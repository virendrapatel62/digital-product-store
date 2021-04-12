
from django.contrib import admin
from django.urls import path, include
from .views.auth import SignupView, LoginView
from .views.home import home, contactus, about
urlpatterns = [
    path('', home, name='home'),
    path('about', about),
    path('contact-us', contactus),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
]
