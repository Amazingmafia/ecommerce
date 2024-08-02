from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    item_count = 0

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))  # Assuming _cart_id returns a single cart ID
            cart_items = CartItem.objects.filter(cart=cart)

            for cart_item in cart_items:
                item_count += cart_item.quantity

        except Cart.DoesNotExist:
            item_count = 0

    return {'item_count': item_count}  # Return as a dictionary to be used in templates
