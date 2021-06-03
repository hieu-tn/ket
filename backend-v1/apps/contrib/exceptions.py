from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class ExpiredSignatureException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Signature has expired')
    default_code = 'signature_expired'


class InvalidSignatureException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Signature is not valid')
    default_code = 'signature_invalid'


class UserExistsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('User already exists')
    default_code = 'user_exists'


class InternalServerError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Internal Server Error')
    default_code = 'internal_server_error'
