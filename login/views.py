from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import LoginForm


def login_view(request):
    """View for logging in a user."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
            # user = authenticate(
            #     username=form.cleaned_data["username"],
            #     password=form.cleaned_data["password"],
            # )
            # if user is not None:
            #     login(request, user)
            #     return redirect("/home")  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
