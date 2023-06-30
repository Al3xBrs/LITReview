from django import forms

from articles import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["headline", "body","picture"]