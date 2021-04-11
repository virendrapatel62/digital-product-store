
from django.contrib import admin
from django.urls import path, include
from .views import home, about, contactus, signup_view
urlpatterns = [
    path('', home, name='home'),
    path('about', about),
    path('contact-us', contactus),
    path('signup', signup_view),
]
