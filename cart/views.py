from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

from checkout.models import Order, OrderLineItem
from datetime import datetime


def view_cart(request):
    return render(request, 'cart/cart.html')


def alter_cart(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))  
    product = get_object_or_404(Product, pk=product_id)
    date = None
    time = None

    if 'increase-quantity' in request.POST:
        cart[product_id] += 1
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')

    if 'decrease-quantity' in request.POST:
        if product_id in cart:
            if cart[product_id] == 1:
                cart.pop(product_id)
                messages.success(request, 'Successfully removed item from cart')
            else:
                if cart[product_id]['session_datetime']:
                    date = list(cart[product_id]['session_datetime'].keys())[0]
                    if len(cart[product_id]['session_datetime'][date]) == 1:
                        cart.pop(product_id)
                        request.session["cart"] = cart
                        request.session.modified = True
                        messages.success(request, 'Successfully removed item from cart')
                    else:
                        cart[product_id]['session_datetime'][date].popitem()
                        request.session["cart"] = cart
                        request.session.modified = True
                        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
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
            messages.success(request, f'Added {product.name} to your cart')

    # This code only run's if the product is a hire room
    if 'add-session' in request.POST:
        if request.POST.get('chosen-time') != 'none':
            date_as_date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
            date = date_as_date.strftime('%d-%m-%Y')
            time = request.POST.get('chosen-time')
            # This is checking that the product is already in the bag
            if product_id in list(cart.keys()):
                # This is checking to see if there is an instance
                # of this product with the same date in the bag
                if date in cart[product_id]['session_datetime'].keys():
                    # This is to ensure that a date and time cannot match
                    if time in cart[product_id]['session_datetime'][date].keys():
                        messages.error(request, 'Unfortunately, this session has already been booked.')
                        return redirect('product_information', product_id=product_id)
                    else:
                        print('This product and date has another product in the bag')
                        cart[product_id]['session_datetime'][date][time] = quantity
                else:
                    print('This product is in bag but not date')
                    cart[product_id]['session_datetime'][date][time] = quantity
            else:
                print('This is the first of this product and date')
                cart[product_id] = {'session_datetime': {date: {time: 1}}}

            request.session["cart"] = cart
            request.session.modified = True
            messages.success(request, f'Added {product.name} session to your cart')
            return redirect('view_cart')
        else:
            messages.error(request, 'You must select a date and time for this session!')
            return redirect('product_information', product_id=product_id)

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

    if 'book' in request.POST:
        # Handle Hire Room Bookings
        return redirect('product_information', product_id=product_id)

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