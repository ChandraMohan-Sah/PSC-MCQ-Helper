from django.shortcuts import render


def home(request):
    context = {
        "title": "Home Page",
        "sidebar_content": "Knowledge Assessment",
    }
    return render(request, "home/home.html", context)


