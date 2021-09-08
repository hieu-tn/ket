import logging
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import EndUserManager, AdminManager
from . import constants as users_constant

logger = logging.getLogger(__name__)


class Status(models.TextChoices):
    FORCE_CHANGE_PASSWORD = 'FORCE_CHANGE_PASSWORD', _('FORCE_CHANGE_PASSWORD')
    ARCHIVED = 'ARCHIVED', _('ARCHIVED')
    CONFIRMED = 'CONFIRMED', _('CONFIRMED')
    UNCONFIRMED = 'UNCONFIRMED', _('UNCONFIRMED')


class User(AbstractUser):
    end_users = EndUserManager()
    admins = AdminManager()

    REQUIRED_FIELDS = []

    user_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_column='uuid', db_index=True)
    status = models.CharField(max_length=40, choices=Status.choices, default=Status.CONFIRMED, null=True, blank=True)
    email = models.EmailField(_('email address'), validators=[users_constant.EMAIL_REGEX], null=True, blank=True)
    phone = models.CharField(validators=[users_constant.PHONE_REGEX], max_length=17, null=True, blank=True)
    attributes = models.JSONField(null=True, blank=True)
