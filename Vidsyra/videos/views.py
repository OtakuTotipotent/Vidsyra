from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
        {"pageTitle": "Home of Intelligence Behind Videos"},
    )
