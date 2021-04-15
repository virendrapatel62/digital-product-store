from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.views import View

# Create your views here.


class SignupView(FormView):
    form_class = UserCreationForm
    template_name = 'store/signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'store/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('login')


'''
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, template_name='store/login.html', context=context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, template_name='store/login.html', context=context)
'''


'''
def LoginView(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, template_name='store/login.html', context=context)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, template_name='store/login.html', context=context)

'''


'''
class SignupView(View):

    def send_response(self, request, context):
        return render(request, template_name='store/signup.html', context=context)

    def get(self, request):
        print("Class based View = Get ")
        form = UserCreationForm()
        context = {
            'form': form
        }
        return self.send_response(request, context)

    def post(self, request):
        print("Class based View = POST ")
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('home')

        return self.send_response(request, context)
'''

'''
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

'''
