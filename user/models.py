# user/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission 
from django.db import models

class CustomUser(AbstractUser):
    mfa_secret = models.CharField(max_length=16, blank=True, null=True)
    mfa_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.email
