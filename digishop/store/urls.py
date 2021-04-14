
from django.contrib import admin
from django.urls import path, include
from .views.auth import SignupView, LoginView
from .views.home import HomeView, contactus, about
from .views.details import product_detail_view
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about),
    path('contact-us', contactus),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('product/<str:slug>', product_detail_view),
]
