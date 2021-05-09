from django.contrib import admin
from .models import Product, Category, Payment, UserProduct
# Register your models here.
from math import floor
from django.utils.html import format_html
from django.db.models import F, Q


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'category', 'get_price',
                    'get_discount', 'get_sale_price', 'active']
    list_editable = ['active']
    list_filter = ['active', 'category']
    actions = ['make_active', 'make_inactive',
               'set_discount_25_percent', 'set_discount_50_percent', 'increase_discount_by_5_percent']
    fieldsets = (
        (
            'General Information', {
                'fields': ('name', 'slug')
            }
        ),
        (
            "Description", {
                "fields": ('description', 'category')
            }
        ),
        (
            "Pricing Information", {
                "fields": ('price', 'discount')
            }
        ),
        (
            "Files", {
                "fields": ('thumbnail', 'file', 'file_size')
            }
        ), (
            None, {
                'fields': ('active',)
            }
        )
    )

    def get_price(self, product):
        return f'Rs. {product.price}'

    def get_discount(self, product):
        return f'{product.discount} %'

    def get_sale_price(self, product):
        sale_price = floor(
            product.price - (product.price * product.discount * 0.01))
        return f'Rs. {sale_price}'

    # action
    def make_active(self, request, queryset):
        queryset.update(active=True)

    # action

    def make_inactive(self, request, queryset):
        queryset.update(active=False)

    # action
    def set_discount_50_percent(self, request, queryset):
        queryset.update(discount=50)

    # action
    def set_discount_25_percent(self, request, queryset):
        queryset.update(discount=25)

    # action
    def increase_discount_by_5_percent(self, request, queryset):
        queryset = queryset.filter(discount__lte=95)
        queryset.update(discount=F('discount')+5)

    get_price.short_description = 'Price'
    get_discount.short_description = 'Discount'
    get_sale_price.short_description = 'Sale price'
    make_active.short_description = 'Make Selected Products Active'
    make_inactive.short_description = 'Make Selected Products InActive'
    set_discount_25_percent.short_description = 'set 25%% Discount'
    set_discount_50_percent.short_description = 'set 50%% Discount'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Payment)
admin.site.register(UserProduct)
