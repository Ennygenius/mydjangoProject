from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html", )


def about(request):
    return render(request, "about.html")


def closed(request):
    return render(request, "closed.png")


def open(request):
    return render(request, "open.png")


def order(request):
    return render(request, "order.html")


