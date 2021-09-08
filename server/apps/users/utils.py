import logging

from django.core.exceptions import ValidationError

from .validations import RegexEmailValidator, RegexPhoneValidator
from ..authentication import constants as auth_constant

logger = logging.getLogger(__name__)


def make_signup_extras(decoded: dict):
    try:
        extras = {
            auth_constant.AUTH_TYPE.SMS.value: {'phone': decoded['username']},
            auth_constant.AUTH_TYPE.MAIL.value: {'email': decoded['username']},
        }.get(decoded['auth_type'], {})
        return extras
    except Exception as e:
        raise e


def validate_field(value: str, user=None, validators=None):
    errors = []
    if validators is None:
        return
    for validator in validators:
        try:
            validator = validator()
            validator.validate(value, user)
        except ValidationError as error:
            errors.append(error)
    if errors:
        raise ValidationError(errors)


def validate_email(email: str, user=None, email_validators=None):
    if email_validators is None:
        email_validators = (RegexEmailValidator,)
    return validate_field(value=email, user=user, validators=email_validators)


def validate_phone(phone: str, user=None, phone_validators=None):
    if phone_validators is None:
        phone_validators = (RegexPhoneValidator,)
    return validate_field(value=phone, user=user, validators=phone_validators)
