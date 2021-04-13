
from django.contrib import admin
from django.urls import path
from app.views import home, save
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('save', save),
]
