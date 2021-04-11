from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, template_name='store/index.html', context={})


def about(request):
    return HttpResponse("About Page")


def contactus(request):
    return HttpResponse("Contact Us")
