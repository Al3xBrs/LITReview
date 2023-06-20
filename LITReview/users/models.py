from django.db import models
from django import forms

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
   

class ConnexionForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe",max_length=20)