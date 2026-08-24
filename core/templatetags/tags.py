from django import template
from order.models import Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def get_cart_items(context):
    request = context['request']

    if not request.user.is_authenticated:
        return []

    cart, _ = Cart.objects.get_or_create(
        user=request.user,
        is_active=True
    )

    return cart.items.select_related('product').all()