import logging

import jwt
from cryptography.hazmat.primitives import serialization
from django.conf import settings

from ..exceptions import ExpiredTokenException, InvalidTokenException

logger = logging.getLogger(__name__)


class JWTService:
    __instance = None
    _secret_key = None
    _public_key = None

    _rsa_algorithm = 'RS256'

    def __init__(self):
        """Virtually private constructor."""
        if self.__instance:
            raise Exception('This class {} is a singleton!'.format('JWTService'))

        JWTService.__instance = self
        f = open(settings.JWT_SIGNING_KEY_PATH, 'rb')
        JWTService.__instance._secret_key = serialization.load_pem_private_key(data=f.read(), password=None)
        f = open(settings.JWT_VERIFYING_KEY_PATH, 'rb')
        JWTService.__instance._public_key = serialization.load_pem_public_key(data=f.read())

    @staticmethod
    def get_instance():
        if not JWTService.__instance:
            JWTService()

        return JWTService.__instance

    def encode_rsa(self, payload: dict):
        try:
            return jwt.encode(payload, self._secret_key, algorithm=self._rsa_algorithm)
        except Exception as e:
            raise e

    def decode_rsa(self, encoded: str):
        try:
            return jwt.decode(encoded, self._public_key, algorithms=[self._rsa_algorithm])
        except jwt.exceptions.ExpiredSignatureError as e:
            logger.error(e.__repr__())
            raise ExpiredTokenException(e)
        except Exception as e:
            logger.error(e.__repr__())
            raise InvalidTokenException(e)
