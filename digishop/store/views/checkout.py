from django.shortcuts import render, redirect
from store.models import Product
from store.forms import CheckoutForm
from django.contrib.auth.decorators import login_required

from digishop.settings import RAZOPRPAY_KEY , PAYMENT_CALLBACK_URL


@login_required(login_url='/login')
def checkout(request, slug):
    user = request.user
    form = CheckoutForm(initial={'email': user.email})
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
        'form': form,
        'RAZOPRPAY_KEY': RAZOPRPAY_KEY,
        'PAYMENT_CALLBACK_URL' : PAYMENT_CALLBACK_URL
    }
    return render(request, template_name='store/checkout.html', context=context)
