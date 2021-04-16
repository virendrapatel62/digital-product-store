from django.shortcuts import render, redirect
from store.models import Product
from store.forms import CheckoutForm
from django.views.decorators.csrf import csrf_exempt
from store.models import Payment, UserProduct

import razorpay

client = razorpay.Client(
    auth=("rzp_test_Z0PZobJeZ714i2", "0lkbPdWkbepv9LIDsrlhiaLB"))


@csrf_exempt
def payment_verify(request):
    if request.method == 'POST':
        print(request.POST)
        razorpay_payment_id = request.POST['razorpay_payment_id']
        razorpay_order_id = request.POST['razorpay_order_id']
        razorpay_signature = request.POST['razorpay_signature']
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(order_id=razorpay_order_id)
        payment.status = "SUCCESS"
        payment.payment_id = razorpay_payment_id
        payment.save()

        user_product = UserProduct(
            user=payment.user, payment=payment, product=payment.product)

        user_product.save()
        return render(request, template_name='store/payment_success.html')


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
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        template_name = 'store/payment.html'
#       create order here
        order_amount = 50000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {
            'email':  email,
            'phone': phone

        }
        data = {
            'amount': order_amount,
            'currency': order_currency,
            'receipt': order_receipt,
            'notes': notes
        }
        order = client.order.create(data=data)

        # create payment
        payment = Payment(product=product, user=user,
                          status='FAIL', order_id=order.get('id'))
        payment.save()
        context = {
            'user': user,
            'product': product,
            'order': order
        }

    else:
        context = {
            'product': product,
            'form': form
        }
        template_name = 'store/checkout.html'

    return render(request, template_name=template_name, context=context)
