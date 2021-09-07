import logging
from enum import Enum, EnumMeta

logger = logging.getLogger(__name__)


class ConstantEnumMeta(EnumMeta):
    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except (TypeError, KeyError) as error:
            return ConstantEnum.DEFAULT


class ConstantEnum(Enum, metaclass=ConstantEnumMeta):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class HttpMethod(ConstantEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    DEFAULT = None


HTTP_METHOD = HttpMethod
