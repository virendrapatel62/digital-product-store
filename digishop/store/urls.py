
from django.contrib import admin
from django.urls import path, include
from .views import home, about, contactus
urlpatterns = [
    path('', home),
    path('about', about),
    path('contact-us', contactus),
]
