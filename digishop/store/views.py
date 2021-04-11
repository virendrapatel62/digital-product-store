from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
        }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, template_name='store/signup.html', context=context)


def home(request):
    return render(request, template_name='store/index.html', context={})


def about(request):
    return HttpResponse("About Page")


def contactus(request):
    return HttpResponse("Contact Us")
