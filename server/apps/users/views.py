import logging

from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.tokens import RefreshToken

from .exceptions import UserExistsException
from .models import User
from .serializers import UserSerializer
from ..contrib.responses import ResourceCreatedResponse
from ..authentication.utils import try_to_activate_unconfirmed_user, prepare_jwt_token_response
from ..authentication.models import ChallengeName
from .utils import validate_email

logger = logging.getLogger(__name__)


class UsersViewSet(viewsets.ViewSet):
    """
    User ViewSet
    """

    permission_classes = ()
    authentication_classes = ()

    def create(self, request, format=None):
        try:
            username, email, password = (
                getattr(request, 'data').get('username'),
                getattr(request, 'data').get('email'),
                getattr(request, 'data').get('password'),
            )

            validate_password(password)
            validate_email(email)

            if User.objects.filter(username=username).exists():
                raise UserExistsException()

            serializer = UserSerializer(
                data={
                    'username': username,
                    'password': make_password(password),
                    'email': email,
                }
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            hash_code = try_to_activate_unconfirmed_user(serializer.instance)
            token = prepare_jwt_token_response(serializer.instance)
        except KeyError as e:
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['username', 'email', 'password']:
                ParseError()
            raise e
        except Exception as e:
            raise e
        else:
            return ResourceCreatedResponse(
                {'challenge': ChallengeName.ACTIVATION_CODE_VERIFIER, 'hash_code': hash_code, **token}
            )
