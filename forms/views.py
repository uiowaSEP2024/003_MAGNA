from django.shortcuts import render


# Create your views here.
def home_page(request):
    """FILL IN"""
    return render(request, "home.html")


def pto(request):
    """FILL IN"""
    return render(request, "pto.html")


def requests(request):
    """FILL IN"""
    return render(request, "requests.html")