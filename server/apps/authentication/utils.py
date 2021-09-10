import logging
import string
from random import choice

from django.conf import settings
from django.contrib.auth.hashers import make_password

from . import constants as auth_constant
from ..users.models import User

logger = logging.getLogger(__name__)


def initiate_activation_code():
    try:
        digits = string.digits
        code = ''.join(choice(digits) for _ in range(auth_constant.ACTIVATION_CODE_LENGTH))
        hash_code = make_password(code, settings.SECRET_KEY)
    except Exception as e:
        raise e
    else:
        return code, hash_code


def try_to_activate_unconfirmed_user(user: User):
    try:
        code, hash_code = initiate_activation_code()

        # mail = MailService.get_instance()
        # mail.send_signup_verification_mail(user.email, code=code)

        # token = make_jwt_access_token_response(user)
        pass
    except Exception as e:
        raise e
    else:
        return
        # return prepare_challenge_response_data(
        #     challenge_name=auth_constant.CHALLENGE_NAME.ACTIVATION_CODE_VERIFIER.value,
        #     data={'hash_code': hash_code, **token}
        # )
