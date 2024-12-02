from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []