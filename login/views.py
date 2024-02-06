from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import LoginForm


def login_view(request):
    """FILL IN"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to a success page.
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
