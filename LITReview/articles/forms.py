from django import forms
from articles import models


class TicketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].widget = forms.Textarea(attrs={"rows": 5, "cols": 80})

    class Meta:
        model = models.Ticket
        fields = ["headline", "body", "picture"]


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].widget = forms.Textarea(attrs={"rows": 3, "cols": 80})

    class Meta:
        model = models.Review
        fields = ["rating", "headline", "body", "picture"]
