from django.contrib.auth.models import UserManager
from django.db import models


class UserQuerySet(models.QuerySet):
    pass


class EndUserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db).filter(is_superuser=False)


class AdminManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db).filter(is_superuser=True)
