import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _, ngettext


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
                ngettext(
                    'This password does not contain enough special characters. It must contain at least %(count)d special characters.',
                    'This password does not contain enough special characters. It must contain at least %(count)d special characters.',
                    self.count,
                ),
                code='password_special_characters_invalid',
                params={'count': self.count},
            )

    def get_help_text(self):
        return (
            ngettext(
                'Your password must contain at least %(count)d special characters.',
                'Your password must contain at least %(count)d special characters.',
                self.count,
            )
            % {'count': self.count}
        )


class RegexEmailValidator:
    """
    Validate whether the email follows a regex
    """

    def __init__(self):
        self.regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    def validate(self, email: str, user=None):
        if re.search(self.regex, email):
            raise ValidationError(
                ngettext(
                    'This email does not follow regex. It must follow %(regex).',
                    'This email does not follow regex. It must follow %(regex).',
                    self.regex,
                ),
                code='email_not_regex',
                params={'regex': self.regex},
            )
