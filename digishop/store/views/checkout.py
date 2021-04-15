from django.shortcuts import render
from store.models import Product
from store.forms import CheckoutForm


def checkout(request, slug):
    form = CheckoutForm()
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
        'form': form
    }
    return render(request, template_name='store/checkout.html', context=context)
