from django import forms


class LoginForm(forms.Form):
    """Form for logging in a user."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
