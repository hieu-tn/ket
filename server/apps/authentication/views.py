import datetime
import logging

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, server_error, AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .challenges import ChallengeSwitcher
from .utils import initiate_activation_code, make_jwt_session_token
from ..contrib.exceptions import ExpiredTokenException, InvalidTokenException
from ..contrib.responses import ResourceCreatedResponse
from ..contrib.services.jwt import JWTService
from ..contrib.utils import map_validation_errors_to_list
from ..notifications.services import Notification, VerificationNotification
from ..users.exceptions import UserDoesNotExistException
from ..users.models import User, Status
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
            jwt_service = JWTService.get_instance()
            decoded = jwt_service.decode_rsa(session_token)
            if make_password(str(code), settings.SECRET_KEY) != decoded['hash_code']:
                raise ParseError('Invalid code')

            decoded.pop('hash_code', None)
            session_token = make_jwt_session_token(
                {
                    **decoded,
                    'exp': auth_constant.SIGNUP_TOKEN_LIFETIME,
                },
                auth_constant.SIGNUP_TOKEN_LIFETIME,
            )
            return Response(data=session_token)
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().replace('\'', '') in ['code', 'session_token']:
                raise ParseError('Payload needs code, sessionToken')
            server_error(request)
        except ExpiredTokenException as e:
            raise AuthenticationFailed(e)
        except InvalidTokenException as e:
            raise ParseError(e)
        except Exception as e:
            logger.error(e.__repr__())
            raise e

    def _get_verification(self, request):
        try:
            target, auth_type = request.data['target'], request.data['auth_type']
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
                    'exp': datetime.datetime.now() + datetime.timedelta(seconds=auth_constant.ACTIVATION_CODE_LIFETIME),
                },
                auth_constant.ACTIVATION_CODE_LIFETIME,
            )
            return Response(data=session_token)
        except ValidationError as e:
            logger.error(e.__repr__())
            raise ParseError(map_validation_errors_to_list(e))
        except Exception as e:
            logger.error(e.__repr__())
            server_error(request)

    def create(self, request, format=None):
        try:
            username, password = (
                getattr(request, 'data').get('username'),
                getattr(request, 'data').get('password'),
            )
            auth = ModelBackend()
            user = auth.authenticate(request, username, password)
            if user is None:
                raise UserDoesNotExistException()

            resp = ChallengeSwitcher.process(user=user)
        except KeyError as e:
            logger.info(e)
            raise ParseError()
        except TypeError as e:
            logger.info(e)
            raise InternalServerError()
        except AttributeError as e:
            logger.info(e)
            raise ParseError()
        except Exception as e:
            raise e
        else:
            return Response(resp)

    @action(methods=['post'], detail=False, url_path='forgot-password', url_name='Forgot Password')
    def forgot_password(self, request, format=None):
        try:
            username = getattr(request, 'data').get('username')

            user = User.objects.get(username=username)
            password = User.objects.make_random_password(
                length=users_constant.PASSWORD_MIN_LENGTH, allowed_chars=users_constant.PASSWORD_ALLOWED_CHARS
            )
            serializer = UserSerializer(user, data={'password': make_password(password)})
            serializer.force_change_password()

            # mail_service = MailService.get_instance()
            # mail_service.send_new_password_mail(email=user.email, password=password)
        except KeyError as e:
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['username']:
                raise ParseError()
            server_error(request)
        except User.DoesNotExist as e:
            raise UserDoesNotExistException()
        except Exception as e:
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
    def respond_to_challenge(self, request, format=None):
        try:
            resp = ChallengeSwitcher.respond(request=request)
        except KeyError as e:
            logger.error(e)
            raise ParseError()
        except TypeError as e:
            logger.error(e)
            server_error(request)
        except AttributeError as e:
            logger.error(e)
            raise ParseError()
        except Exception as e:
            raise e
        else:
            return Response(resp)
