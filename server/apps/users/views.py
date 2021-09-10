import logging

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import viewsets
from rest_framework.exceptions import ParseError, server_error, ValidationError, AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import constants as users_constant
from .exceptions import UserExistsException
from .models import User
from .permissions import UserAccessOneOwnRecordPermission, IsUserConfirmed
from .serializers import UserSerializer
from .utils import make_signup_extras
from ..authentication.tokens import decode_jwt_untyped_token
from ..contrib.exceptions import ExpiredTokenException, InvalidTokenException
from ..contrib.responses import ResourceCreatedResponse
from ..contrib.utils import map_validation_errors_to_list

logger = logging.getLogger(__name__)


class UsersViewSet(viewsets.GenericViewSet):
    """
    User ViewSet
    """

    authentication_classes = []
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_uuid'

    def get_authenticators(self):
        """
        Instantiates and returns the list of authenticators that this view can use.
        """
        authentication_classes = self.authentication_classes
        if self.detail:
            authentication_classes.append(JWTAuthentication)
        return [auth() for auth in authentication_classes]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = self.permission_classes
        if self.detail:
            permission_classes.extend([UserAccessOneOwnRecordPermission, IsUserConfirmed])
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            untyped_token, password = request.data['untyped_token'], request.data['password']
            decoded, _ = decode_jwt_untyped_token(untyped_token)
            validate_password(password)

            if self.get_queryset().filter(username=decoded['username']).exists():
                raise UserExistsException()

            extras = make_signup_extras(decoded)
            g = Group.objects.get(name=users_constant.USER_GROUP.END_USER.value)
            serializer = self.get_serializer_class()(
                data={
                    'username': decoded['username'],
                    'password': make_password(password),
                    'groups': [g.id],
                    **extras,
                }
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['untyped_token', 'password']:
                raise ParseError('Payload needs untypedToken, password')
            elif e.__str__().translate(str.maketrans('', '', '\'')) in ['username']:
                raise ValidationError('Invalid untypedToken')
            return server_error(request)
        except ExpiredTokenException as e:
            logger.error(e.__repr__())
            raise AuthenticationFailed(e)
        except InvalidTokenException as e:
            logger.error(e.__repr__())
            raise ValidationError(e)
        except DjangoValidationError as e:
            logger.error(e.__repr__())
            raise ValidationError(map_validation_errors_to_list(e))
        except Exception as e:
            logger.error(e.__repr__())
            raise e
        else:
            return ResourceCreatedResponse()

    def retrieve(self, request, user_uuid=None):
        try:
            serializer = self.get_serializer_class()(self.get_object())
            data = serializer.data
            data['groups'] = data.get('user_groups')
            excluded_keys = [
                'id',
                'password',
                'is_superuser',
                'is_staff',
                'is_active',
                'user_permissions',
                'user_groups',
            ]
            data = {k: v for k, v in data.items() if k not in excluded_keys}
            return Response(data)
        except Exception as e:
            logger.error(e.__repr__())
            raise e
