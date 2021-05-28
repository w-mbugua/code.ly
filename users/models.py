from django.db import models
from django.contrib.auth.models import AbstractUser


class Customuser(AbstractUser):
    location = models.CharField(max_length=50, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
