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


class UserHasNotConfirmedException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('User has not confirmed yet')
    default_code = 'user_not_confirmed'


class UserHasBeenArchivedException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('User has been archived')
    default_code = 'user_archived'


class UserHasConfirmedException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _('User already confirmed')
    default_code = 'user_confirmed'


class PasswordValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Password is invalid')
    default_code = 'password_invalid'
