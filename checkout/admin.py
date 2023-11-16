from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("line_item_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "total_cost",
        "original_cart",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "total_cost",
        "original_cart",
        "stripe_pid",
    )

    list_display = ("order_number", "full_name", "date", "total_cost")

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
