from django import forms


class LoginForm(forms.Form):
    """FILL IN"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
