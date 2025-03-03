from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    favourite_team = models.CharField(max_length=50, blank=True, null=True)