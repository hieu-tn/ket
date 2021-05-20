from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework.response import Response


class ExpiredSignatureException(APIException):
    status_code = 401
    default_detail = _('Signature has expired')
    default_code = 'signature_expired'


class InvalidSignatureException(APIException):
    status_code = 400
    default_detail = _('Signature is not valid')
    default_code = 'signature_invalid'


class UserExistsException(APIException):
    status_code = 400
    default_detail = _('User already exists')
    default_code = 'user_exists'


class InternalServerError(APIException):
    status_code = 500
    default_detail = _('Internal Server Error')
    default_code = 'internal_server_error'


class ResourceCreatedResponse(Response):
    status_code = 201
    default_detail = _('Resource created')
    default_code = 'resource_created'
