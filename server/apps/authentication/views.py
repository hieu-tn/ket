import logging

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .challenges import ChallengeSwitcher
from ..contrib.exceptions import InternalServerError
from ..contrib.responses import ResourceCreatedResponse
from ..mails.services import MailService
from ..users.exceptions import UserDoesNotExistException, UserHasNotConfirmedException
from ..users.models import User, Status
from ..users.serializers import UserSerializer
from ..users import constants as users_constant

logger = logging.getLogger(__name__)


class AuthenticationViewSet(viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()

    www_authenticate_realm = 'api'

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

            mail_service = MailService.get_instance()
            mail_service.send_new_password_mail(email=user.email, password=password)
        except KeyError as e:
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['username']:
                raise ParseError()
            raise InternalServerError()
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
            raise InternalServerError()
        except AttributeError as e:
            logger.error(e)
            raise ParseError()
        except Exception as e:
            raise e
        else:
            return Response(resp)
