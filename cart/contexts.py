from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    cart_products = []
    product_count = 0
    total = 0
    cart = request.session.get("cart", {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_products.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                    "item_subtotal": item_data * product.price,
                }
            )
        else:
            product = get_object_or_404(Product, pk=item_id)
            for date, time in item_data["session_datetime"].items():
                quantity = len(time)
                total += quantity * product.price
                product_count += quantity
                cart_products.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "date": date,
                        "time": time,
                        "item_subtotal": quantity * product.price,
                    }
                )

    context = {
        "cart_products": cart_products,
        "product_count": product_count,
        "total": total,
    }

    return context
