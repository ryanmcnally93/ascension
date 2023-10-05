from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def alter_cart(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))  
    date = ""

    product = get_object_or_404(Product, pk=product_id)

    if 'date' in request.POST:
        date = request.POST.get('date')
        # NEEDS TO BE THE SELECTED TIME
        time = request.POST.get('time')
        print(date)
        print(time)
        # UPDATE BOOKED SESSIONS?

    if 'increase-quantity' in request.POST:
        cart[product_id] += 1
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')

    if 'decrease-quantity' in request.POST:
        if product_id in cart:
            if cart[product_id] == 1:
                cart.pop(product_id)
                messages.success(request, 'Successfully removed item from bag')
            else:
                cart[product_id] -= 1
                messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
        else:
            messages.error(request, 'This item isnt in the cart!')

    if 'add-quantity' in request.POST:
        if product_id in list(cart.keys()):
            cart[product_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
        else:
            cart[product_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    if 'remove_all_of_item_product_info' in request.POST:
        try:
            if product_id in cart:
                cart.pop(product_id)
                request.session['cart'] = cart
                messages.success(request, 'Successfully removed item from bag')
                return redirect('product_information', product_id=product_id)
            else: 
                messages.error(request, 'This item isnt in the cart!')
        except Exception as e:
            messages.error(request, f'Error removing item {e}')
            return HttpResponse(status=500)

    if 'remove_all_of_item_cart' in request.POST:
        try:
            if product_id in cart:
                cart.pop(product_id)
                request.session['cart'] = cart
                messages.success(request, 'Successfully removed item from bag')
                return redirect('view_cart')
            else:
                messages.error(request, 'This item isnt in the cart!')
        except Exception as e:
            messages.error(request, f'Error removing item {e}')
            return HttpResponse(status=500)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
    # HttpResponse('<script>history.back();</script>')
