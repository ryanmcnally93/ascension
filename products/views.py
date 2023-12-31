from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from checkout.models import Order, OrderLineItem
from cart.contexts import cart_contents
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProductForm


def products(request):
    products = Product.objects.all().order_by('id')
    categories = None
    sort = None
    direction = None
    category = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            category = request.GET["category"].upper().replace("_", " ")

        if "sort" in request.GET:
            sort = request.GET["sort"]
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sort = f"-{sort}"
            products = products.order_by(sort)

        if "shop" in request.GET:
            products = products.filter(is_hire_room=False)

        if "sale" in request.GET:
            products = products.filter(is_offers_item=True)

    current_sort = f"{sort}_{direction}"

    context = {
        "products": products,
        "current_sort": current_sort,
        "category": category,
    }
    return render(request, "products/products.html", context)


def product_information(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    stringed_product_id = str(product.id)

    # This will be a list of all the saved purchases of this item
    takentimes = []

    # We want to look through all orders
    orders = Order.objects.all()

    # Only do this if we are on a session page
    if product.is_hire_room:
        # Look through every order
        for order in orders:
            # Look at every item
            for item in order.lineitems.all():
                # Only add to the list if they have the same product id
                # As we are giving the item itself
                # we can manipulate the dates and times is a cool way
                if item.product.id == product_id:
                    takentimes.append(item)

    if "cart" in request.session:
        if stringed_product_id in request.session["cart"]:
            item_quantity = request.session["cart"][stringed_product_id]
        else:
            item_quantity = ""
    else:
        item_quantity = ""

    # This variable is used by the radio buttons
    sessions = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]

    # This variable is used in the slideshow
    images = []
    if product.main_image:
        images.append(product.main_image)
    if product.image:
        images.append(product.image)
    if product.image_2:
        images.append(product.image_2)
    if product.image_3:
        images.append(product.image_3)

    context = {
        "product": product,
        "stringed_product_id": stringed_product_id,
        "item_quantity": item_quantity,
        "sessions": sessions,
        "images": images,
        "takentimes": takentimes,
    }
    return render(request, "products/product_information.html", context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_information", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )

    else:
        form = ProductForm()

    template = "products/add_products.html"
    context = {
        "form": form,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def edit_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    products = Product.objects.all()
    product = None
    form = ProductForm()

    if "product-id" in request.POST:
        product_id = request.POST.get("product-id", False)
        if product_id == "None":
            messages.error(request, "You need to select an item to edit.")
            return redirect("edit_product")
        else:
            product = get_object_or_404(Product, name=product_id)
            form = ProductForm(instance=product)

    if "product" in request.GET:
        product_id = request.GET["product"]
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)

    if request.method == "POST" and "product-id" not in request.POST:
        name = request.POST.get("name", False)
        product = get_object_or_404(Product, name=name)
        form = ProductForm(request.POST, request.FILES, instance=product)
        striked_price = request.POST.get("striked_price")
        if form.is_valid():
            if striked_price:
                product.is_offers_item = True
            else:
                product.is_offers_item = False
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_information", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )

    template = "products/edit_products.html"
    context = {
        "form": form,
        "on_profile_page": True,
        "product": product,
        "products": products,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
