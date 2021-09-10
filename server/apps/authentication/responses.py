import logging

from . import constants as auth_constant

logger = logging.getLogger(__name__)


class ChallengeResponse:
    __challenge: None
    __data: None

    def __init__(
        self,
        name: auth_constant.CHALLENGE_NAME = auth_constant.CHALLENGE_NAME.NO_CHALLENGE,
        data: dict = {},
    ):
        self.__challenge = name.value
        self.__data = data

    def __call__(self):
        return {'challenge': self.__challenge, **self.__data}
