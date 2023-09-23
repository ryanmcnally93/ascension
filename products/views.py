from django.shortcuts import render, get_object_or_404
from .models import Product


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
    context = {
        'product': product,
    }
    return render(request, 'products/product_information.html', context)
