from django.shortcuts import HttpResponse, redirect
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
    return JsonResponse({"title": "My First Blog", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea com" })
