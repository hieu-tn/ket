import logging

from django.core.exceptions import ValidationError

from .validations import RegexEmailValidator, RegexPhoneValidator

logger = logging.getLogger(__name__)


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
