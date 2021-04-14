from django.shortcuts import HttpResponse, render
from store.models import Product


def product_detail_view(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, template_name='store/product_detail.html', context=context)
