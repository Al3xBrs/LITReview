from django.shortcuts import redirect
from django.contrib.auth import logout


def reg_user(request):
    pass


def logout_user(request):
    logout(request)
    return redirect('login')


