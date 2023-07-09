from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django import forms


class Ticket(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=120, verbose_name="Titre")
    body = models.CharField(max_length=1000, blank=True, verbose_name="Commentaire")
    upvote = models.PositiveIntegerField(blank=True, null=True)
    picture = models.ImageField(verbose_name="Image de l'article", blank=True)

class Review(models.Model):
    rate = [
        ("0",0),
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("5",5),
    ]
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, blank=True)
    rating = models.CharField(max_length=1, choices=rate)
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


