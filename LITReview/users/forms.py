from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email", "profile_picture"]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
