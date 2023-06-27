from django.shortcuts import render, redirect
from users.forms import ConnexionForm, UserForm
from django.contrib.auth import authenticate, login

def Inscription(request):
    if request.method == "POST":

        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('homepage')
    else:
        form = UserForm()

    return render(request, "users/inscription.html", {"form" : form})

def Connexion(request):
    form = ConnexionForm()
    message = ""
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"], 
                password = form.cleaned_data["password"],
                )
           
            if user is not None:
                print("ok")
                login(request, user)
                message = f"Bonjour {user.pseudo}"
            else:
                print("non ok")
                message = "Identifiants invalides."

    return render(request, "users/connexion.html", {"form" : form, "message":message})


def Homepage(request):
    return render(request, "users/index.html")