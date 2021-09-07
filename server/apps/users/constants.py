import string

from django.core.validators import RegexValidator

from ..contrib.constants import ConstantEnum

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
    code='invalid_phone_regex',
)
email_regex = RegexValidator(
    regex=r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
    message='Email must be entered in the format: "johndoe@example.com"',
    code='invalid_email_regex',
)


class UserGroup(ConstantEnum):
    END_USER = 'END_USER'
    ADMIN = 'ADMIN'


PASSWORD_ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation
PASSWORD_MIN_LENGTH = 8
PHONE_REGEX = phone_regex
EMAIL_REGEX = email_regex
USER_GROUP = UserGroup
