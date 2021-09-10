import logging

from django.conf import settings
from django.contrib.auth.hashers import make_password

from . import constants as auth_constant
from .tokens import make_jwt_session_token, make_jwt_access_token
from ..users.exceptions import UserHasNotConfirmedException, UserHasBeenArchivedException
from ..users.models import User
from .responses import ChallengeResponse

logger = logging.getLogger(__name__)


class ChallengeSwitcher:
    """
    Challenge Switcher
    """

    @classmethod
    def process(cls, user: User, *args, **kwargs):
        try:
            challenge_name = user.status.lower()
            method_name = '_process_challenge_' + challenge_name
            method = getattr(cls, method_name, lambda: 'Invalid challenge name')
            return method(cls, user, *args, **kwargs)
        except Exception as e:
            raise e

    def _process_challenge_force_change_password(self, user: User, *args, **kwargs):
        try:
            token = make_jwt_session_token(payload={
                'user_uuid': str(user.user_uuid),
                'hash_user_uuid': make_password(str(user.user_uuid), settings.SECRET_KEY)
            }, expires_in=auth_constant.SESSION_TOKEN_LIFETIME)
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(
                name=auth_constant.CHALLENGE_NAME.NEW_PASSWORD_REQUIRED,
                data={'user_uuid': user.user_uuid, **token},
            )

    def _process_challenge_confirmed(self, user: User, *args, **kwargs):
        try:
            token = make_jwt_access_token(user)
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(data={'user_uuid': user.user_uuid, **token})()

    def _process_challenge_archived(self, *args, **kwargs):
        raise UserHasBeenArchivedException()

    def _process_challenge_unconfirmed(self, *args, **kwargs):
        raise UserHasNotConfirmedException()
