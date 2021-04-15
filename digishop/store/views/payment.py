from django.shortcuts import render, redirect
from store.models import Product
from store.forms import CheckoutForm


def create_payment(request, slug):
    template_name = ''
    context = {}
    form = CheckoutForm(request.POST)
    product = Product.objects.get(slug=slug)
    user = None
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login')
    if form.is_valid():
        print("create payment")
        template_name = 'store/payment.html'
        context = {
            'user': user,
            'product': product
        }
    else:
        context = {
            'product': product,
            'form': form
        }
        template_name = 'store/checkout.html'

    return render(request, template_name=template_name, context=context)
