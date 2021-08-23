from ..contrib.constants import ConstantEnum


class Channel(ConstantEnum):
    MAIL = 'MAIL'
    SMS = 'SMS'
    DEFAULT = None


CHANNEL = Channel
