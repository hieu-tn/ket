import logging
import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from . import constants as users_constant

logger = logging.getLogger(__name__)


class SpecialCharactersPasswordValidator:
    """
    Validate whether the password contains special characters
    """

    def __init__(self, count=1):
        self.count = count

    def validate(self, password, user=None):
        password = password.lower().strip().replace(' ', '')
        password = re.sub(r"""\d*|\s*|\w*""", '', password)
        if len(password) < self.count:
            raise ValidationError(
                message='This password does not contain enough special characters. It must contain at least {} special characters.'.format(
                    self.count
                ),
                code='password_special_characters_invalid',
                params={'count': self.count},
            )

    def get_help_text(self):
        return 'Your password must contain at least {} special characters.'.format(self.count)


class RegexEmailValidator:
    """
    Validate whether the email follows a regex
    """

    def __init__(self):
        self.regex = users_constant.EMAIL_REGEX

    def validate(self, email: str, user=None):
        self.regex.__call__(email)


class RegexPhoneValidator:
    """
    Validate whether the email follows a regex
    """

    def __init__(self):
        self.regex = users_constant.PHONE_REGEX

    def validate(self, phone: str, user=None):
        self.regex.__call__(phone)
