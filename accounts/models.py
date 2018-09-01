from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomAccount(AbstractUser):
    # add additional fields in here
    is_seller = models.BooleanField(default=False)
    def __str__(self):
        return self.email