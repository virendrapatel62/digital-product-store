from django.contrib import admin
from .models import Product, Category, Payment, UserProduct
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(UserProduct)
