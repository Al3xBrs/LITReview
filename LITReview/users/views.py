import users
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
import articles
from django.contrib.auth.decorators import login_required

def signup_page(request):
    form = users.forms.SignupForm()
    if request.method == 'POST':
        form = users.forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'users/inscription.html', {'form': form})

@login_required
def profil_page(request, user_id):
    user = users.models.User.objects.get(id=user_id)
    tickets = articles.models.Ticket.objects.filter(user = user).order_by("-time_created")
    reviews = articles.models.Review.objects.filter(user = user).order_by("-time_created")
    return render(request, "users/profil_user.html", {"user":user, "tickets":tickets, "reviews":reviews})








