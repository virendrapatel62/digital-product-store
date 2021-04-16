from django.shortcuts import render, redirect
from store.models import UserProduct
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

# @login_required(login_url='/login')


@method_decorator(login_required(login_url='/login'), name='dispatch')
class OrderListView(ListView):
    template_name = 'store/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user = self.request.user
        return UserProduct.objects.filter(
            user=user).order_by('-payment__date')
