from users import forms, models
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from articles import models as art_mod
from django.contrib.auth.decorators import login_required


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "users/inscription.html", {"form": form})


@login_required
def profil_page(request, user_id):
    user_check = models.User.objects.get(id=user_id)
    tickets = art_mod.Ticket.objects.filter(user=user_check).order_by("-time_created")
    reviews = art_mod.Review.objects.filter(user=user_check).order_by("-time_created")
    followed = user_check.followers
    return render(
        request,
        "users/profil_user.html",
        {
            "user_check": user_check,
            "tickets": tickets,
            "reviews": reviews,
            "followed": followed,
        },
    )


@login_required
def follow_user(request, user_id):
    user_check = models.User.objects.get(id=user_id)
    user = request.user
    user.followers.add(user_check)
    return redirect("profil_page", user_id)


@login_required
def unfollow_user(request, user_id):
    user_check = models.User.objects.get(id=user_id)
    user = models.User.objects.get(id=request.user.id)
    user.followers.remove(user_check)
    return redirect("profil_page", user_id)
