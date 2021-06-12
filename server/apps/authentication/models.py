from django.db import models
from django.utils.translation import gettext_lazy as _


class ChallengeName(models.TextChoices):
    ACTIVATION_CODE_VERIFIER = 'ACTIVATION_CODE_VERIFIER', _('ACTIVATION_CODE_VERIFIER')
    NEW_PASSWORD_REQUIRED = 'NEW_PASSWORD_REQUIRED', _('NEW_PASSWORD_REQUIRED')
