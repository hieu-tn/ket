from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    objects = CustomUserManager()
