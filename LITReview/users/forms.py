from django import forms
from users.models import User

class ConnexionForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe",max_length=20, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
