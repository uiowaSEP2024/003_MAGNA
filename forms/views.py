from django.shortcuts import render


# Create your views here.
def home_page(request):
    """FILL IN"""
    return render(request, "home.html")
