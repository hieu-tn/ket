from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class ExpiredTokenException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Token has expired')
    default_code = 'token_expired'


class InvalidTokenException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Token is not valid')
    default_code = 'token_invalid'


class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Internal Server Error')
    default_code = 'internal_server_error'
