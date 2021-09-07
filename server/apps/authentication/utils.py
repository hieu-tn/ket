import logging
import string
from random import choice

from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from . import constants as auth_constant
from .models import ChallengeName
from ..contrib.services.jwt import JWTService
from ..users.models import User
from . import constants as authentication_constant

logger = logging.getLogger(__name__)


def make_jwt_session_token(payload: dict, expires_in: int):
    try:
        jwt_service = JWTService.get_instance()
        session_token = jwt_service.encode_rsa(payload)
        return {'session_token': session_token, 'expires_in': expires_in}
    except Exception as e:
        raise e


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

        token = make_jwt_access_token_response(user)
    except Exception as e:
        raise e
    else:
        return prepare_challenge_response_data(
            challenge_name=ChallengeName.ACTIVATION_CODE_VERIFIER.value, data={'hash_code': hash_code, **token}
        )


def make_jwt_access_token_response(user: User):
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
