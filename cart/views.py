from django.shortcuts import render, redirect
from django.http import HttpResponse


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))
    
    #THIS IS WHERE THE PROBLEM IS
    # date = ""
    # if request.POST.get('date-time') == "":
    #     print('YES')
    #PROBLEM

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

    request.session['cart'] = cart
    print(request.session['cart'])
    return HttpResponse('<script>history.back();</script>')
