import datetime
import logging

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import Token, RefreshToken, UntypedToken as SimpleJWTUntypedToken

from . import constants as auth_constant
from ..users.models import User

logger = logging.getLogger(__name__)


class SessionToken(Token):
    token_type = 'session'
    lifetime = datetime.timedelta(seconds=auth_constant.SESSION_TOKEN_LIFETIME)


class UnTypedToken(SimpleJWTUntypedToken):
    lifetime = datetime.timedelta(seconds=auth_constant.UNTYPED_TOKEN_LIFETIME)


class KetToken(RefreshToken):
    @property
    def session_token(self):
        """
        Returns a session token created from this refresh token.  Copies all
        claims present in this refresh token to the new session token except
        those claims listed in the `no_copy_claims` attribute.
        """
        session = SessionToken()

        # Use instantiation time of refresh token as relative timestamp for
        # session token "exp" claim.  This ensures that both a refresh and
        # session token expire relative to the same time if they are created as
        # a pair.
        session.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            session[claim] = value

        return session

    @property
    def untyped_token(self):
        """
        Returns a untyped token created from this refresh token.  Copies all
        claims present in this refresh token to the new untyped token except
        those claims listed in the `no_copy_claims` attribute.
        """
        untyped = UnTypedToken()

        # Use instantiation time of refresh token as relative timestamp for
        # session token "exp" claim.  This ensures that both a refresh and
        # session token expire relative to the same time if they are created as
        # a pair.
        untyped.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            untyped[claim] = value

        return untyped

    @classmethod
    def for_payload(cls, payload: dict):
        """
        Returns an authorization token for the given payload.
        """
        token = cls()
        for k, v in payload.items():
            token[k] = v

        return token


def make_jwt_session_token(user: User):
    try:
        token = KetToken.for_user(user)
        return {
            'session_token': str(token.session_token),
            'expires_in': auth_constant.SESSION_TOKEN_LIFETIME,
        }
    except Exception as e:
        raise e


def make_jwt_access_token(user: User):
    try:
        token = KetToken.for_user(user)
        return {
            'access_token': str(token.access_token),
            'expires_in': auth_constant.ACCESS_TOKEN_LIFETIME,
        }
    except Exception as e:
        raise e


def make_jwt_untyped_token(payload: dict):
    try:
        token = KetToken.for_payload(payload)
        return {
            'untyped_token': str(token.untyped_token),
            'expires_in': auth_constant.UNTYPED_TOKEN_LIFETIME,
        }
    except Exception as e:
        raise e


def decode_jwt_untyped_token(raw_token: str):
    """
    Validates an encoded token and returns a validated token wrapper object.
    """
    messages = []
    try:
        validated_token = UnTypedToken(raw_token)
        return validated_token.payload, validated_token
    except TokenError as e:
        messages.append({'token_class': UnTypedToken.__name__,
                         'token_type': UnTypedToken.token_type,
                         'message': e.args[0]})

    raise DjangoValidationError(
        message=messages,
        code='untyped_token_invalid',
    )
