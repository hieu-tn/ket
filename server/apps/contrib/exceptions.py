from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class ExpiredTokenException(Exception):
    pass


class InvalidTokenException(Exception):
    pass
