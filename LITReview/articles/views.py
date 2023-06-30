from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articles.forms import TicketForm
from articles import models

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'articles/home.html', {"tickets": tickets})

@login_required
def ticket_upload(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    
    return render(request, 'articles/ticket-upload.html', {"form":form})

