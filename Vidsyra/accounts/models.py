from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Vidsyra user account; starts with Django's standard username auth."""

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username
