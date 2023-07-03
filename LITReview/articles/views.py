from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articles.forms import TicketForm, ReviewForm
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

@login_required
def ticket_detail(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    return render(request, 'articles/ticket-detail.html', {"ticket":ticket})

@login_required
def ticket_delete(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    ticket.delete()
    return redirect("home")

@login_required
def ticket_delete_view(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    return render(request, "articles/ticket-delete.html", {"ticket":ticket})

@login_required
def review_upload(request, ticket_id):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = models.Ticket.objects.get(id=ticket_id)
            review.save()
            return redirect(f'ticket_detail/{ticket_id}')
        
    return render(request, 'articles/review-upload.html', {"form":form})