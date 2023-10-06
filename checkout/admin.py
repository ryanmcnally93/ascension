from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total_cost')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'postcode', 'town_or_city', 
              'street_address1', 'street_address2', 'total_cost')

    list_display = ('order_number', 'full_name', 'date', 'total_cost')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
# 6:44
# 7:03
