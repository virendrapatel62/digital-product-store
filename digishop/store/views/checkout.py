from django.shortcuts import render, redirect
from store.models import Product
from store.forms import CheckoutForm


def checkout(request, slug):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login')

    form = CheckoutForm(initial={'email': user.email})
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
        'form': form
    }
    return render(request, template_name='store/checkout.html', context=context)
