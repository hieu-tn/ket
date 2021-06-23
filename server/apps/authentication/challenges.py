import logging

from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..contrib.exceptions import InternalServerError
from ..users.exceptions import UserHasNotConfirmedException, UserHasBeenArchivedException
from ..users.models import Status
from .responses import ChallengeResponse

logger = logging.getLogger(__name__)


class ChallengeSwitcher:
    """
    Challenge Switcher
    """

    @classmethod
    def process_challenge(cls, *args, **kwargs):
        try:
            challenge_name = kwargs.get('user').status.lower()
            method_name = '_process_challenge_' + challenge_name
            method = getattr(cls, method_name, lambda: 'Invalid challenge name')
            return method(cls, *args, **kwargs)
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['name']:
                raise ParseError()
            raise InternalServerError()
        except AttributeError as e:
            raise ParseError()
        except Exception as e:
            raise e

    def _process_challenge_force_change_password(self, *args, **kwargs):
        try:
            user = kwargs.get('user')
            refresh = RefreshToken.for_user(user)
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(
                name=Status.FORCE_CHANGE_PASSWORD,
                data={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
            )

    def _process_challenge_confirmed(self, *args, **kwargs):
        try:
            user = kwargs.get('user')
            refresh = RefreshToken.for_user(user)
        except Exception as e:
            raise e
        else:
            return ChallengeResponse(
                data={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
            )

    def _process_challenge_archived(self, *args, **kwargs):
        raise UserHasBeenArchivedException()

    def _process_challenge_unconfirmed(self, *args, **kwargs):
        raise UserHasNotConfirmedException()
