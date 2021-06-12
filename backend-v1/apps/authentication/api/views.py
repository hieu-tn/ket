import logging

from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES

from ..challenges import ChallengeSwitcher
from ...contrib import constants as constant
from ...contrib.exceptions import InternalServerError
from ...contrib.responses import ResourceCreatedResponse
from ...mails.services import MailService
from ...users.exceptions import UserDoesNotExistException, UserHasNotConfirmedException
from ...users.models import User

logger = logging.getLogger(__name__)


class AuthViewSet(viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()

    www_authenticate_realm = 'api'

    def create(self, request, format=None):
        try:
            username, password = getattr(request, 'data')['username'], getattr(request, 'data')['password']
            auth = ModelBackend()
            user = auth.authenticate(request, username, password)
            if user is None:
                raise UserDoesNotExistException()

            resp = ChallengeSwitcher.process_challenge(user=user)
        except KeyError as e:
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['username', 'password']:
                raise ParseError()
            raise e
        except Exception as e:
            raise e
        else:
            return resp

    @action(methods=['post'], detail=False, url_path='forgot-password', url_name='Forgot Password')
    def forgot_password(self, request, format=None):
        try:
            username = getattr(request, 'data').get('username')

            user = User.objects.get(username=username)
            user.update_status_force_change_password()
            new_pwd = User.objects.make_random_password(
                length=constant.PASSWORD_MIN_LENGTH, allowed_chars=constant.PASSWORD_ALLOWED_CHARS
            )
            user.save_password(new_pwd)

            mail_service = MailService.get_instance()
            mail_service.send_new_password_mail(email=user.email, password=new_pwd)
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['username']:
                raise ParseError()
            raise InternalServerError()
        except User.DoesNotExist as e:
            raise UserDoesNotExistException()
        except User.NotConfirmed as e:
            raise UserHasNotConfirmedException()
        except Exception as e:
            raise e
        else:
            return ResourceCreatedResponse()

    @action(methods=['post'], detail=False, url_path='challenge', url_name='Respond to challenge')
    def respond_to_challenge(self, request, format=None):
        try:
            pass
            # return ChallengeSwitcher.respond_challenge(request=request)
        except Exception as e:
            raise e
