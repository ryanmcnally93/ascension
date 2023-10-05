from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse
from products.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def alter_cart(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))  
    date = ""

    product = Product.objects.get(pk=product_id)

    if 'date' in request.POST:
        date = request.POST.get('date')
        # NEEDS TO BE THE SELECTED TIME
        time = request.POST.get('time')
        print(date)
        print(time)
        # UPDATE BOOKED SESSIONS?

    if 'increase-quantity' in request.POST:
        cart[product_id] += 1

    if 'decrease-quantity' in request.POST:
        if product_id in cart:
            if cart[product_id] == 1:
                cart.pop(product_id)
            else:
                cart[product_id] -= 1
        else:
            # This is an issue! Reload issue causing this.
            print('This item isnt in the cart!')

    if 'add-quantity' in request.POST:
        if product_id in list(cart.keys()):
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    if 'remove_all_of_item_product_info' in request.POST:
        if product_id in cart:
            cart.pop(product_id)
            print('I AM SUCCESSFULLY RUNNING CORRECT CODE!')
            request.session['cart'] = cart
            return redirect('product_information', product_id=product_id)
        else: 
            # This is an issue! Reload issue causing this.
            print('This item isnt in the cart!')

    if 'remove_all_of_item_cart' in request.POST:
        if product_id in cart:
            cart.pop(product_id)
            request.session['cart'] = cart
            return redirect('view_cart')
        else: 
            # This is an issue! Reload issue causing this.
            print('This item isnt in the cart!')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
    # HttpResponse('<script>history.back();</script>')
