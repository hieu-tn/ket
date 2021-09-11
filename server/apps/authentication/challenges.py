import logging

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError, PermissionDenied as DjangoPermissionDenied

from . import constants as auth_constant
from .tokens import make_jwt_session_token, make_jwt_access_token
from .utils import initiate_activation_code
from ..contrib.exceptions import InternalError
from ..notifications import constants as notifications_constant
from ..notifications.services import Notification, VerificationNotification
from ..users.models import User
from .responses import ChallengeResponse
from ..users.serializers import UserSerializer

logger = logging.getLogger(__name__)


class ChallengeSwitcher:
    """
    Challenge Switcher
    """

    @classmethod
    def process(cls, user: User, *args, **kwargs):
        try:
            status_name = user.status.lower()
            method_name = '_process_' + status_name
            method = getattr(cls, method_name)
            return method(cls, user, *args, **kwargs)
        except AttributeError as e:
            raise InternalError(e)
        except Exception as e:
            raise e

    def _process_force_change_password(self, user: User, *args, **kwargs):
        try:
            token = make_jwt_session_token({
                'user_uuid': str(user.user_uuid),
                'hash_user_uuid': make_password(str(user.user_uuid), settings.SECRET_KEY),
            })
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(
                name=auth_constant.CHALLENGE_NAME.NEW_PASSWORD_REQUIRED,
                data={'user_uuid': user.user_uuid, **token},
            )()

    def _process_confirmed(self, user: User, *args, **kwargs):
        try:
            token = make_jwt_access_token(user)
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(data={'user_uuid': user.user_uuid, **token})()

    def _process_archived(self, *args, **kwargs):
        raise DjangoPermissionDenied()

    def _process_unconfirmed(self, user: User, *args, **kwargs):
        try:
            code, hash_code = initiate_activation_code()
            channel = notifications_constant.CHANNEL.SMS if user.phone else None
            Notification.send(user, VerificationNotification(code)).via(channel)
            token = make_jwt_session_token({
                'user_uuid': str(user.user_uuid),
                'hash_user_uuid': make_password(str(user.user_uuid), settings.SECRET_KEY),
                'hash_code': hash_code,
            })
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(
                name=auth_constant.CHALLENGE_NAME.ACTIVATION_CODE_VERIFIER,
                data={'user_uuid': user.user_uuid, **token},
            )()

    @classmethod
    def respond(cls, user: User, payload: dict, *args, **kwargs):
        try:
            challenge_name = payload['challenge'].lower()
            method_name = '_respond_' + challenge_name
            method = getattr(cls, method_name)
            return method(cls, user, payload, *args, **kwargs)
        except AttributeError as e:
            raise InternalError(e)
        except Exception as e:
            raise e

    def _respond_new_password_required(self, user: User, payload: dict, *args, **kwargs):
        try:
            raw_password = payload['password']
            validate_password(raw_password)

            serializer = UserSerializer(user, data={'password': make_password(raw_password)})
            serializer.confirm()
            return self.process(user)
        except Exception as e:
            raise e

    def _respond_activation_code_verifier(self, user: User, payload: dict, *args, **kwargs):
        try:
            code = payload['code']
            if make_password(code, settings.SECRET_KEY) != payload['hash_code']:
                raise DjangoValidationError(message='Invalid code', code='invalid_code')

            serializer = UserSerializer(user)
            serializer.confirm()
            return self.process(user)
        except Exception as e:
            raise e

    def _respond_mfa(self, user: User, payload: dict, *args, **kwargs):
        try:
            return
        except Exception as e:
            raise e
