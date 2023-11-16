from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import truncatechars

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # This code means the user cannot enter just spaces and save
            for field in form:
                if len(field.value().lstrip(" ")) == 0:
                    messages.error(request, "Please do not leave fields empty")
                    return redirect("profile")
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order {truncatechars(order_number, 8)}."
            f'A confirmation email was sent on {order.date.strftime("%d-%m-%Y")}.'
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
