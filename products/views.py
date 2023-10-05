from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.contexts import cart_contents


def products(request):
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort = f'-{sort}'
            products = products.order_by(sort)

        if 'shop' in request.GET:
            products = products.filter(is_hire_room=False)

        if 'sale' in request.GET:
            products = products.filter(is_offers_item=True)

    current_sort = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_sort': current_sort,
    }
    return render(request, 'products/products.html', context)


def product_information(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
            
    stringed_product_id = str(product.id)

    if stringed_product_id in request.session['cart']:
        item_quantity = request.session['cart'][stringed_product_id]
    else:
        item_quantity = ""

    sessions = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]
    booked_sessions = ["10:00"]

    context = {
        'product': product,
        'stringed_product_id': stringed_product_id,
        'item_quantity': item_quantity,
        'sessions': sessions,
        'booked_sessions': booked_sessions,
    }
    return render(request, 'products/product_information.html', context)
    
