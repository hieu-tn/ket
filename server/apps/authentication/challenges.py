import logging

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.authentication import JWTAuthentication

from .utils import try_to_activate_unconfirmed_user, prepare_jwt_token_response, prepare_challenge_response_data
from ..contrib.exceptions import InternalServerError
from ..contrib.responses import ResourceCreatedResponse
from ..users.exceptions import (
    UserHasBeenArchivedException,
    UserDoesNotExistException,
    PasswordValidationError,
)
from ..users.models import User, Status
from ..users.serializers import UserSerializer
from .exceptions import InvalidChallengeException
from .models import ChallengeName

logger = logging.getLogger(__name__)


class ChallengeSwitcher:
    """
    Challenge Switcher
    """

    @classmethod
    def respond(cls, *args, **kwargs):
        try:
            request = kwargs.get('request')
            challenge = getattr(request, 'data').get('challenge').lower()
            method_name = '_respond_' + challenge
            method = getattr(cls, method_name, lambda: InvalidChallengeException())
            return method(cls, *args, **kwargs)
        except Exception as e:
            raise e

    def _respond_activation_code_verifier(self, *args, **kwargs):
        try:
            request = kwargs.get('request')
            code = getattr(request, 'data').get('code').__str__()
            hash_code = getattr(request, 'data').get('hash_code')

            if make_password(code, settings.SECRET_KEY) != hash_code:
                raise ParseError()

            user = request.user
            serializer = UserSerializer(user)
            serializer.confirm()
        except KeyError as e:
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['code']:
                raise ParseError()
            raise InternalServerError()
        except User.DoesNotExist as e:
            raise UserDoesNotExistException()
        except ValidationError as e:
            raise ParseError([{'code': err.code, 'messages': err.messages} for err in e.error_list])
        except Exception as e:
            raise e
        else:
            return prepare_challenge_response_data(challenge_name='')

    def _respond_new_password_required(self, *args, **kwargs):
        try:
            request = kwargs.get('request')
            user = request.user
            password = getattr(request, 'data').get('password')

            validate_password(password=password, user=user)

            serializer = UserSerializer(user, data={'password': make_password(password), 'status': Status.CONFIRMED})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except ValidationError as e:
            raise PasswordValidationError([{'code': err.code, 'messages': err.messages} for err in e.error_list])
        except Exception as e:
            raise e
        else:
            return prepare_challenge_response_data(challenge_name='')

    @classmethod
    def process(cls, *args, **kwargs):
        try:
            challenge = kwargs.get('user').status.lower()
            method_name = '_process_' + challenge
            method = getattr(cls, method_name, lambda: InvalidChallengeException())
            return method(cls, *args, **kwargs)
        except Exception as e:
            raise e

    def _process_force_change_password(self, *args, **kwargs):
        try:
            user = kwargs.get('user')
            token = prepare_jwt_token_response(user)
        except Exception as e:
            raise e
        else:
            return prepare_challenge_response_data(
                challenge_name=ChallengeName.NEW_PASSWORD_REQUIRED.value, data={**token}
            )

    def _process_confirmed(self, *args, **kwargs):
        try:
            user = kwargs.get('user')
            token = prepare_jwt_token_response(user)
        except Exception as e:
            raise e
        else:
            return prepare_challenge_response_data(challenge_name='', data={**token})

    def _process_archived(self, *args, **kwargs):
        raise UserHasBeenArchivedException()

    def _process_unconfirmed(self, *args, **kwargs):
        try:
            user = kwargs.get('user')
            resp = try_to_activate_unconfirmed_user(user)
        except Exception as e:
            raise e
        else:
            return resp
