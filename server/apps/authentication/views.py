import logging

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError as DjangoValidationError, PermissionDenied as DjangoPermissionDenied
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, server_error, ValidationError, PermissionDenied
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .challenges import ChallengeSwitcher
from .tokens import make_jwt_session_token, decode_jwt_session_token
from .utils import initiate_activation_code
from ..contrib.exceptions import InternalError
from ..contrib.utils import map_validation_errors_to_list
from ..notifications.services import Notification, VerificationNotification, ForgotPasswordNotification
from ..users.exceptions import UserDoesNotExistException
from ..users.models import User
from ..users.serializers import UserSerializer
from ..users import constants as users_constant
from ..notifications import constants as notifications_constant
from . import constants as auth_constant
from ..contrib import constants as contrib_constant
from ..users.utils import validate_phone, validate_email

logger = logging.getLogger(__name__)


class AuthenticationViewSet(viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()

    www_authenticate_realm = 'api'

    def create(self, request):
        try:
            username, password = request.data['username'], request.data['password']
            authenticated_user = ModelBackend().authenticate(request, username, password)

            if not authenticated_user:
                raise UserDoesNotExistException()

            resp = ChallengeSwitcher.process(user=authenticated_user)
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['username', 'password']:
                raise ParseError('Payload needs username, password')
            return server_error(request)
        except InternalError as e:
            logger.error(e.__repr__())
            return server_error(request)
        except DjangoPermissionDenied as e:
            raise PermissionDenied(e)
        except Exception as e:
            logger.error(e.__repr__())
            raise e
        else:
            return Response(resp)

    @action(methods=['post', 'get'], detail=False, url_path='verification', url_name='Verify anonymous user')
    def verification(self, request):
        try:
            if request.method == contrib_constant.HTTP_METHOD.POST.value:
                return self._post_verification(request)
            elif request.method == contrib_constant.HTTP_METHOD.GET.value:
                return self._get_verification(request)
        except Exception as e:
            raise e

    def _post_verification(self, request):
        try:
            code, session_token = request.data['code'], request.data['session_token']
            decoded, _ = decode_jwt_session_token(session_token)
            if make_password(str(code), settings.SECRET_KEY) != decoded['hash_code']:
                raise ValidationError('Invalid code')

            decoded.pop('hash_code', None)
            session_token = make_jwt_session_token(payload=decoded)
            return Response(data=session_token)
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['code', 'session_token']:
                raise ParseError('Payload needs code, sessionToken')
            return server_error(request)
        except DjangoValidationError as e:
            logger.error(e.__repr__())
            raise ValidationError(map_validation_errors_to_list(e))
        except Exception as e:
            logger.error(e.__repr__())
            raise e

    def _get_verification(self, request):
        try:
            target, auth_type = request.data['target'], request.data['auth_type'].upper()
            user = {}
            if auth_type == auth_constant.AUTH_TYPE.SMS.value:
                validate_phone(target)
                user['phone'] = target
            elif auth_type == auth_constant.AUTH_TYPE.MAIL.value:
                validate_email(target)
                user['email'] = target
            else:
                raise ParseError('Invalid authType')

            code, hash_code = initiate_activation_code()
            Notification.send(user, VerificationNotification(code)).via(notifications_constant.CHANNEL(auth_type))
            session_token = make_jwt_session_token(
                {
                    'hash_code': hash_code,
                    'username': target,
                    'auth_type': auth_type,
                }
            )
            return Response(data=session_token)
        except DjangoValidationError as e:
            logger.error(e.__repr__())
            raise ValidationError(map_validation_errors_to_list(e))
        except Exception as e:
            logger.error(e.__repr__())
            raise e

    @action(methods=['post'], detail=False, url_path='forgot-password', url_name='Forgot Password')
    def forgot_password(self, request):
        try:
            username, auth_type = request.data['username'], request.data['auth_type'].upper()

            user = User.end_users.get(username=username)
            password = User.objects.make_random_password(
                length=users_constant.PASSWORD_MIN_LENGTH, allowed_chars=users_constant.PASSWORD_ALLOWED_CHARS
            )
            serializer = UserSerializer(user, data={'password': make_password(password)})
            serializer.force_change_password()

            Notification.send(user, ForgotPasswordNotification(password)).via(notifications_constant.CHANNEL(auth_type))
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['username', 'auth_type']:
                raise ParseError('Payload needs username, authType')
            return server_error(request)
        except User.DoesNotExist as e:
            logger.error(e.__repr__())
            return Response()
        except Exception as e:
            logger.error(e.__repr__())
            raise e
        else:
            return Response()

    @action(
        methods=['post'],
        detail=False,
        url_path='challenge',
        url_name='Respond to challenge',
        authentication_classes=(JWTAuthentication,),
    )
    def respond_to_challenge(self, request):
        try:
            user_uuid, session_token = request.data['user_uuid'], request.data['session_token']
            decoded, _ = decode_jwt_session_token(session_token)

            if user_uuid != decoded['user_uuid'] or make_password(user_uuid, settings.SECRET_KEY) != decoded['hash_user_uuid']:
                raise ValidationError('Invalid user uuid')

            user = User.end_users.get(user_uuid=user_uuid)
            resp = ChallengeSwitcher.respond(user=user, payload={**decoded, **request.data})
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['challenge', 'user_uuid', 'session_token', 'password', 'code']:
                raise ParseError('Payload needs challenge, userUuid, sessionToken and password/code')
            return server_error(request)
        except InternalError as e:
            logger.error(e.__repr__())
            return server_error(request)
        except DjangoValidationError as e:
            logger.error(e.__repr__())
            raise ValidationError(map_validation_errors_to_list(e))
        except Exception as e:
            logger.error(e.__repr__())
            raise e
        else:
            return Response(resp)
