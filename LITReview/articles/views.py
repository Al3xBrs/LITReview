from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articles.forms import TicketForm, ReviewForm
from articles import models
from itertools import chain
from django.db.models import CharField, Value


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value("ticket", CharField()))
    reviews = models.Review.objects.all()
    reviews = reviews.annotate(content_type=Value("review", CharField()))
    posts = sorted(
        chain(tickets, reviews), key=lambda post: post.time_created, reverse=True
    )
    return render(request, "articles/home.html", {"posts": posts})


@login_required
def followed(request):
    user = request.user
    followed = user.followers
    reviews = models.Review.objects.all()
    reviews = reviews.annotate(content_type=Value("review", CharField()))
    tickets = models.Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value("ticket", CharField()))
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
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
def edit_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("ticket_detail", ticket_id)
    else:
        form = TicketForm(instance=ticket)
    return render(request, "articles/edit_ticket.html", {"form": form})


@login_required
def edit_review(request, review_id):
    review = models.Review.objects.get(id=review_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ReviewForm(instance=review)
    return render(request, "articles/edit_review.html", {"form": form})


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
def review_delete(request, review_id):
    review = models.Review.objects.get(id=review_id)
    ticket = models.Ticket.objects.get(id=review.ticket.id)
    ticket.review_posted = False
    ticket.save()
    review.delete()

    return redirect("home")


@login_required
def review_delete_view(request, review_id):
    review = models.Review.objects.get(id=review_id)
    return render(request, "articles/review-delete.html", {"review": review})


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
