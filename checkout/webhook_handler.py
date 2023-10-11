from django.http import HttpResponse
import stripe


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        total = round(stripe_charge.amount / 100, 2)
        
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        try:
            order = Order.objects.get(
                full_name__iexact=billing_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=billing_details.phone,
                postcode__iexact=billing_details.postal_code,
                town_or_city__iexact=billing_details.city,
                street_address1__iexact=billing_details.line1,
                street_address2__iexact=billing_details.line2,
                total__iexact=total,
                )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    postcode=billing_details.postal_code,
                    town_or_city=billing_details.city,
                    street_address1=billing_details.line1,
                    street_address2=billing_details.line2,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
