from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    products = Product.objects.all()
    category = None

    if request.GET:
        if category in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)

    context = {
        'products': products,
    }
    print(category)
    return render(request, 'products/products.html', context)


def product_information(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_information.html', context)
