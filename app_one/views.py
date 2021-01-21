from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse


def root(request):
    return redirect("/blogs")


def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("Placeholder to display a new form  to create a new blog")


def create(request):
    return redirect("/")


def show(request, number):
    show_string = f"Placeholder to display blog number: {number}"
    return HttpResponse(show_string)


def edit(request, number):
    edit_string = f"Placeholder to edit blog {number}"
    return HttpResponse(edit_string)


def destroy(request, number):
    return redirect("/blogs")
# Create your views here.


def json(request):
    return JsonResponse({"title": "My First Blog", "content": "Lorem" })


def index2(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
