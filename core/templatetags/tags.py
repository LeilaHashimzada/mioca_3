from django import template
from order.models import Cart


register = template.Library()

@register.simple_tag
def get_cart_items():
    cart, _ = Cart.objects.get_or_create()
    return cart.items.select_related('product').all()