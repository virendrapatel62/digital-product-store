from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from store.models import Product, Category
from django.views import View
from django.views.generic import ListView
# Create your views here.


class HomeView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_context_data(self):
        category_pk = self.request.GET.get("category")
        categories = Category.objects.all()
        if category_pk:
            products = Product.objects.filter(category=category_pk)

        else:
            products = Product.objects.all()

        context = {
            'categories': categories,
            'products': products,

        }

        return context


'''
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, template_name='store/index.html', context=context)

'''


def about(request):
    return HttpResponse("About Page")


def contactus(request):
    return HttpResponse("Contact Us")
