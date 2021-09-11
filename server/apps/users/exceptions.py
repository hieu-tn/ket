import logging

from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)


class UserExistsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('User already exists')
    default_code = 'user_exists'


class UserDoesNotExistException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('User does not exist')
    default_code = 'user_not_exist'
