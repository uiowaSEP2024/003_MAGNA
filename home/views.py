from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """FILL IN"""
    return render(request, "home.html")
