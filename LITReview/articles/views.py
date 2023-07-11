from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articles.forms import TicketForm, ReviewForm
from articles import models
from itertools import chain
from django.db.models import CharField, Value


@login_required
def home(request):
    tickets = models.Ticket.objects.all().order_by("-time_created")
    reviews = models.Review.objects.all()
    return render(
        request, "articles/home.html", {"tickets": tickets, "reviews": reviews}
    )


# TODO: Vue file d'abonnement
@login_required
def followed(request):
    user = request.user
    followed = user.followers
    reviews = models.Review.objects.all().order_by("-time_created")
    reviews = reviews.annotate(content_type=Value("review", CharField()))
    tickets = models.Ticket.objects.all().order_by("-time_created")
    tickets = tickets.annotate(content_type=Value("ticket", CharField()))
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created)
    return render(
        request,
        "articles/followed.html",
        {"followed": followed, "posts": posts},
    )


@login_required
def ticket_upload(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")

    return render(request, "articles/ticket-upload.html", {"form": form})


@login_required
def ticket_detail(request, ticket_id):
    reviews = models.Review.objects.filter(ticket=ticket_id).order_by("-time_created")
    ticket = models.Ticket.objects.get(id=ticket_id)
    return render(
        request, "articles/ticket-detail.html", {"ticket": ticket, "reviews": reviews}
    )


@login_required
def ticket_delete(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    ticket.delete()
    return redirect("home")


@login_required
def ticket_delete_view(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    return render(request, "articles/ticket-delete.html", {"ticket": ticket})


@login_required
def review_upload(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            ticket.review_posted = True
            ticket.save()
            return redirect("ticket_detail", ticket_id)

    return render(
        request, "articles/review-upload.html", {"form": form, "ticket": ticket}
    )


@login_required
def review_up(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("home")

    return render(request, "articles/review-upload.html", {"form": form})
