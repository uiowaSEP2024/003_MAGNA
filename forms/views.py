from django.shortcuts import render


# Create your views here.
def home_page(request):
    """FILL IN"""
    return render(request, "home.html")


def absence_request(request):
    """FILL IN"""
    return render(request, "absence_request.html")


def requests(request):
    """FILL IN"""
    return render(request, "requests.html")