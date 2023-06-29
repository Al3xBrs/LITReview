from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class User(AbstractUser):
    """ """

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["username","password"]
    USERNAME_FIELD = "email"
    profile_picture = models.ImageField(verbose_name="Image de profil")







