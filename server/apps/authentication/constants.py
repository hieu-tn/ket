from ..contrib import constants as contrib_constant


class AuthType(contrib_constant.ConstantEnum):
    DEFAULT = None
    SMS = 'SMS'
    MAIL = 'MAIL'


ACTIVATION_CODE_LENGTH = 6
ACTIVATION_CODE_LIFETIME = 60 * 60 * 24 * 365  # 1 year

ACCESS_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
REFRESH_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
SLIDING_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
SLIDING_TOKEN_REFRESH_LIFETIME = 60 * 60 * 24 * 365  # 1 year

SIGNUP_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year

AUTH_TYPE = AuthType
