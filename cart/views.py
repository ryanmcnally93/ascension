from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

from checkout.models import Order, OrderLineItem


def view_cart(request):
    return render(request, 'cart/cart.html')


def alter_cart(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # booked_sessions = request.session.get('booked_sessions', {})
    quantity = int(request.POST.get('quantity'))  
    product = get_object_or_404(Product, pk=product_id)

    #     datetime = f'{date}{time}'
    #     if product_id in booked_sessions:
    #         booked_sessions[product_id] += [f'{date}/{time}']
    #         request.session['booked_sessions'] = booked_sessions
    #         print(booked_sessions)
    #         return redirect('view_cart')
    #     else:
    #         booked_sessions[product_id] = [f'{date}/{time}']
    #         request.session['booked_sessions'] = booked_sessions
    #         print(booked_sessions)
    #         return redirect('view_cart')

    if 'increase-quantity' in request.POST:
        cart[product_id] += 1
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')

    if 'decrease-quantity' in request.POST:
        if product_id in cart:
            if cart[product_id] == 1:
                cart.pop(product_id)
                messages.success(request, 'Successfully removed item from cart')
            else:
                cart[product_id] -= 1
                messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
        else:
            messages.error(request, 'This item isnt in the cart!')

    if 'add-quantity' in request.POST:
        if 'date' in request.POST:
                print('WATCH VIDEOS ON ADDING SIZES FOR ADDING HOURS, THIS ITEM WAS ALREADY IN CART')

        if product_id in list(cart.keys()):
            cart[product_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
        else:
            cart[product_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    if 'remove_all_of_item_product_info' in request.POST:
        try:
            if product_id in cart:
                cart.pop(product_id)
                request.session['cart'] = cart
                messages.success(request, 'Successfully removed item from cart')
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
                messages.success(request, 'Successfully removed item from cart')
                return redirect('view_cart')
            else:
                messages.error(request, 'This item isnt in the cart!')
        except Exception as e:
            messages.error(request, f'Error removing item {e}')
            return HttpResponse(status=500)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def empty_cart(request):
    cart = request.session.get('cart', {})
    if 'empty_cart' in request.POST:
        try:
            cart.clear()
            request.session['cart'] = cart
            messages.success(request, 'Successfully emptied the cart')
            return redirect('view_cart')
        except Exception as e:
            messages.error(request, f'Error emptying cart {e}')
            return HttpResponse(status=500)
    
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('view_cart')