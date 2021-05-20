from django.contrib.auth.models import UserManager
from django.db import models


class UserQuerySet(models.QuerySet):
    pass


class CustomUserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
