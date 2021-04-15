
from django.contrib import admin
from django.urls import path, include
from .views.auth import SignupView, LoginView,  logout_view
from .views.home import HomeView, contactus, about
from .views.details import ProductDetailView
from .views.checkout import checkout
from .views.payment import create_payment
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about),
    path('contact-us', contactus),
    path('logout', logout_view, name='logout'),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('product/<str:slug>', ProductDetailView.as_view()),

    path('checkout/<str:slug>', checkout, name='checkout'),
    path('payment/<str:slug>', create_payment, name='create_payment')
]
