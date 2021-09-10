from ..contrib import constants as contrib_constant


class AuthType(contrib_constant.ConstantEnum):
    SMS = 'SMS'
    MAIL = 'MAIL'


class ChallengeName(contrib_constant.ConstantEnum):
    ACTIVATION_CODE_VERIFIER = 'ACTIVATION_CODE_VERIFIER'
    NEW_PASSWORD_REQUIRED = 'NEW_PASSWORD_REQUIRED'
    MFA = 'MFA'
    NO_CHALLENGE = ''


ACTIVATION_CODE_LENGTH = 6

ACCESS_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
REFRESH_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
SLIDING_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
SLIDING_TOKEN_REFRESH_LIFETIME = 60 * 60 * 24 * 365  # 1 year
SESSION_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year
UNTYPED_TOKEN_LIFETIME = 60 * 60 * 24 * 365  # 1 year

AUTH_TYPE = AuthType
CHALLENGE_NAME = ChallengeName
