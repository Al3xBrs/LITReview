from django.db import models


class User(models.Model):
    pseudo = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)
   


