import logging
import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

logger = logging.getLogger(__name__)

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
)


class Status(models.TextChoices):
    FORCE_CHANGE_PASSWORD = 'FORCE_CHANGE_PASSWORD', _('FORCE_CHANGE_PASSWORD')
    ARCHIVED = 'ARCHIVED', _('ARCHIVED')
    CONFIRMED = 'CONFIRMED', _('CONFIRMED')
    UNCONFIRMED = 'UNCONFIRMED', _('UNCONFIRMED')


class User(AbstractUser):
    objects = CustomUserManager()

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=40, choices=Status.choices, default=Status.UNCONFIRMED, null=True, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
