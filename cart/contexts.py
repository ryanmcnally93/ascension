from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_products = []
    product_count = 0
    total = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            cart_products.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

    context = {
        'cart_products': cart_products,
        'product_count': product_count,
        'total': total,
    }

    return context
