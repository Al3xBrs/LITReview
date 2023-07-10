from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField



class User(AbstractUser):
    """ """

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["username","password"]
    USERNAME_FIELD = "email"
    profile_picture = ResizedImageField(size=[100,100],upload_to="media/profile_images/",verbose_name="Image de profil", blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True)








