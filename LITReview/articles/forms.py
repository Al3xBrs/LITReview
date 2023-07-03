from django import forms

from articles import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["headline", "body","picture"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["rating", "headline", "body"]