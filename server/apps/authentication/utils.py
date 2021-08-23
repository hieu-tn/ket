import logging
import string
from random import choice

from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from . import constants as auth_constant
from .models import ChallengeName
from ..users.models import User
from . import constants as authentication_constant

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

        token = prepare_jwt_token_response(user)
    except Exception as e:
        raise e
    else:
        return prepare_challenge_response_data(
            challenge_name=ChallengeName.ACTIVATION_CODE_VERIFIER.value, data={'hash_code': hash_code, **token}
        )


def prepare_jwt_token_response(user: User):
    try:
        refresh = RefreshToken.for_user(user)
    except Exception as e:
        raise e
    else:
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'expires_in': authentication_constant.ACCESS_TOKEN_LIFETIME,
        }


def prepare_challenge_response_data(challenge_name: str = None, **kwargs):
    try:
        data = {}
        if 'data' in kwargs:
            data = kwargs.get('data')

        return {'challenge_name': challenge_name, **data}
    except Exception as e:
        raise e
