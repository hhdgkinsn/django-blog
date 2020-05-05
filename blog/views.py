from django.shortcuts import render
from .services.fetch import fetchData


def home(request):
    context = {
        "posts": fetchData
    }
    return render(request, "blog/home.html", context)
