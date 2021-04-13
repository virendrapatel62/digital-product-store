from django import template
from math import floor

register = template.Library()


@register.simple_tag()
def sale_price(price, discount):
    print(price, discount)
    return floor(price - (price * discount * 0.01))
