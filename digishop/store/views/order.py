from django.shortcuts import render, redirect
from store.models import UserProduct


def OrderListView(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login')

    orders = UserProduct.objects.filter(user=user)
    return render(request, template_name='store/orders.html', context={'orders': orders})
