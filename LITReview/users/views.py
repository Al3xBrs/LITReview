from django.shortcuts import render

def Inscription(request):
    return render(request, "users/inscription.html")

def Connexion(request):
    return render(request, "users/connexion.html")