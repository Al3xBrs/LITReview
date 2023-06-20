from django.shortcuts import render
from users.models import ConnexionForm

def Inscription(request):
    return render(request, "users/inscription.html")

def Connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():

            return render(request, "users/connexion.html", {"form" : form})
    
    else:
        form =  ConnexionForm()
        return render(request, "users/connexion.html", {"form" : form})