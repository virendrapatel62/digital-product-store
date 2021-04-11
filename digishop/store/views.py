from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Hello World..")


def about(request):
    return HttpResponse("About Page")


def contactus(request):
    return HttpResponse("Contact Us")
