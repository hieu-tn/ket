import logging

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

logger = logging.getLogger(__name__)


class Status(models.TextChoices):
    FORCE_CHANGE_PASSWORD = 'FORCE_CHANGE_PASSWORD', _('FORCE_CHANGE_PASSWORD')
    ARCHIVED = 'ARCHIVED', _('ARCHIVED')
    CONFIRMED = 'CONFIRMED', _('CONFIRMED')
    UNCONFIRMED = 'UNCONFIRMED', _('UNCONFIRMED')


class User(AbstractUser):
    objects = CustomUserManager()

    status = models.CharField(max_length=40, choices=Status.choices, default=Status.UNCONFIRMED, null=True, blank=True)

    def update_status_force_change_password(self):
        try:
            if self.status == Status.UNCONFIRMED:
                raise self.NotConfirmed()

            self.update_status(Status.FORCE_CHANGE_PASSWORD)
        except Exception as e:
            raise e

    def update_status(self, status: Status.choices):
        try:
            self.status = status
            self.save()
        except Exception as e:
            raise e

    def save_password(self, raw_pwd: str):
        try:
            self.set_password(raw_pwd)
            self.save(update_fields=['password'])
        except Exception as e:
            raise e

    class NotConfirmed(Exception):
        pass
