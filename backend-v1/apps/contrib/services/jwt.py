import os
import re
from typing import Dict, Any

import jwt

from ..exceptions import ExpiredSignatureException, InvalidSignatureException


class JwtService:
    """
    Jwt Service Singleton
    """

    __instance = None
    _secret_key = None
    _public_key = None
    _rsa_algorithm = 'RS256'

    def __init__(self):
        """Virtually private constructor."""
        if JwtService.__instance is not None:
            raise Exception('This class {} is a singleton!'.format('JwtService'))

        JwtService.__instance = self
        JwtService._secret_key = re.sub('\\n', '\n', os.environ.get('JWT_SIGNING_KEY', 'ket'))
        JwtService._public_key = re.sub('\\n', '\n', os.environ.get('JWT_VERIFYING_KEY', 'ket'))

    @staticmethod
    def get_instance():
        """Static access method."""
        if JwtService.__instance is None:
            JwtService()
        return JwtService.__instance

    def encode_using_rsa(self, payload: Dict[str, Any]):
        try:
            encoded = jwt.encode(payload=payload, key=self._secret_key, algorithm=self._rsa_algorithm)
        except Exception as e:
            raise e
        else:
            return encoded

    def decode_using_rsa(self, encoded: str):
        try:
            payload = jwt.decode(encoded, key=self._public_key, algorithms=[self._rsa_algorithm])
        except jwt.ExpiredSignatureError as e:
            raise ExpiredSignatureException()
        except (jwt.InvalidSignatureError, jwt.InvalidTokenError) as e:
            raise InvalidSignatureException()
        except Exception as e:
            raise e
        else:
            return payload
