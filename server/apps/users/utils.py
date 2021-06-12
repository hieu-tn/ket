from django.core.exceptions import ValidationError

from .validations import RegexEmailValidator


def validate_email(email: str, user=None, email_validators=None):
    errors = []
    if email_validators is None:
        email_validators = (RegexEmailValidator,)
    for validator in email_validators:
        try:
            validator.validate(email, user)
        except ValidationError as error:
            errors.append(error)
    if errors:
        raise ValidationError(errors)
