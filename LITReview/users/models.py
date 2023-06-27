from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser,UserManager
from uuid import uuid4

class User(AbstractBaseUser):



    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (CREATOR, "Créateur"),
        (SUBSCRIBER, "Abonné"),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, default=f"user_{uuid4()}")

    REQUIRED_FIELDS = ["username","password"]
    USERNAME_FIELD = "email"
    objects = UserManager()






