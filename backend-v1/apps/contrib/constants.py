import string

EMAIL_REGEX = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
PASSWORD_REGEX = '.*(?=.{8,})((?=.*[!@#$%^&*()\\-_=+{};:,<.>]){1})(?=.*\\d)((?=.*[a-z]){1})((?=.*[A-Z]){1}).*'
SIGN_UP_EXPIRATION = 60 * 60 * 24
PASSWORD_ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation
PASSWORD_MIN_LENGTH = 12
