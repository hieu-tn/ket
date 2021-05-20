import datetime
import logging

from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer
from ...contrib import constants as constant
from ...contrib.exceptions import UserExistsException, ResourceCreatedResponse
from ...contrib.services.jwt import JwtService
from ...mails.services import MailService

logger = logging.getLogger(__name__)


class UsersViewSet(viewsets.ViewSet):
    """
    User ViewSet
    """

    def create(self, request, format=None):
        try:
            username, email, password = request.data['username'], request.data['email'], request.data['password']
            if User.objects.filter(username=username).exists():
                raise UserExistsException()

            user = UserSerializer(
                data={
                    'username': username,
                    'password': make_password(password),
                    'email': email,
                }
            )
            if user.is_valid(raise_exception=True):
                user.save()

            token = self.generate_signup_token(request)
            self.send_signup_mail(request, token)
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['username', 'email', 'password']:
                ParseError()
            raise e
        except Exception as e:
            raise e
        else:
            return ResourceCreatedResponse()

    def send_signup_mail(self, request, token: str) -> None:
        try:
            email = request.data['email']
            mail = MailService.get_instance()
            mail.send_signup_verification_mail(email=email, token=token)
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['email']:
                ParseError()
            raise e
        except Exception as e:
            raise e

    def generate_signup_token(self, request) -> str:
        try:
            username, email = request.data['username'], request.data['email']

            jwt = JwtService.get_instance()
            token = jwt.encode_using_rsa(
                {
                    'exp': datetime.datetime.now() + datetime.timedelta(seconds=constant.SIGN_UP_EXPIRATION),
                    'username': username,
                    'email': email,
                }
            )
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['username', 'email']:
                ParseError()
            raise e
        except Exception as e:
            raise e
        else:
            return token
