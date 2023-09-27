

def cart_contents(request):

    cart_products = []
    product_count = 0
    total = 0

    context = {
        'cart_products': cart_products,
        'product_count': product_count,
        'total': total,
    }

    return context