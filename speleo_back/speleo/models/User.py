from django.db import models
from django.contrib.auth.models import AbstractUser
from ..managers import UserManager


class User(AbstractUser):
    """User model."""

    username = None
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
