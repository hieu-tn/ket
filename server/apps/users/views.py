import logging

from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from rest_framework.exceptions import ParseError, server_error, ValidationError, AuthenticationFailed

from .exceptions import UserExistsException
from .models import User
from .serializers import UserSerializer
from ..contrib.exceptions import ExpiredTokenException, InvalidTokenException
from ..contrib.responses import ResourceCreatedResponse
from ..authentication.utils import try_to_activate_unconfirmed_user, make_jwt_access_token_response
from ..authentication.models import ChallengeName
from ..contrib.services.jwt import JWTService

logger = logging.getLogger(__name__)


class UsersViewSet(viewsets.GenericViewSet):
    """
    User ViewSet
    """

    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, format=None):
        try:
            session_token, password = request.data['session_token'], request.data['password']
            jwt_service = JWTService().get_instance()
            decoded = jwt_service.decode_rsa(session_token)
            validate_password(password)

            if self.get_queryset().filter(username=decoded['username']).exists():
                raise UserExistsException()

            serializer = self.get_serializer_class()(
                data={
                    'username': decoded['username'],
                    'password': make_password(password),
                }
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            hash_code = try_to_activate_unconfirmed_user(serializer.instance)
            token = make_jwt_access_token_response(serializer.instance)
        except KeyError as e:
            logger.error(e.__repr__())
            if e.__str__().translate(str.maketrans('', '', '\'')) in ['session_token', 'password']:
                raise ParseError('Payload needs sessionToken, password')
            elif e.__str__().translate(str.maketrans('', '', '\'')) in ['username']:
                raise ValidationError('Invalid sessionToken')
            server_error(request)
        except ExpiredTokenException as e:
            logger.error(e.__repr__())
            raise AuthenticationFailed(e)
        except InvalidTokenException as e:
            logger.error(e.__repr__())
            raise ValidationError(e)
        except Exception as e:
            logger.error(e.__repr__())
            server_error(request)
        else:
            return ResourceCreatedResponse(
                {'challenge': ChallengeName.ACTIVATION_CODE_VERIFIER, 'hash_code': hash_code, **token}
            )
