from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """ """

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["username","password"]
    USERNAME_FIELD = "email"
    profile_picture = models.ImageField(upload_to="media/profile_images/",verbose_name="Image de profil", blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True)








