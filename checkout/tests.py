from django.test import TestCase
from .models import Order, OrderLineItem
from decimal import *
from datetime import date


class OrderTestCase(TestCase):
    # Lets test the Order model
    # Here we are creating two new orders
    def setUp(self):
        Order.objects.create(
            order_number='1234567',
            full_name='Michael Owen',
            email='mike@outlook.com',
            phone_number='07382422545',
            street_address1='21 Madeup Road',
            street_address2='Middleof Nowhere',
            town_or_city='Birmingham',
            postcode='B54 3RF',
            total_cost='49.97',
            original_cart='a new football',
            stripe_pid='randomstripestuff1',
        )
        Order.objects.create(
            order_number='5678901',
            full_name='John Smith',
            email='john@blueyonder.com',
            phone_number='07833924711',
            street_address1='14 Somewhere Street',
            street_address2='Random Area',
            town_or_city='Coventry',
            postcode='C32 1RF',
            total_cost='31.56',
            original_cart='a new name',
            stripe_pid='randomstripestuff2',
        )

    # This test is going to check the order number of each, making sure they match
    def test_order_number(self):
        first_order = Order.objects.get(full_name="Michael Owen")
        second_order = Order.objects.get(full_name="John Smith")
        self.assertEqual(first_order.order_number, '1234567')
        self.assertEqual(second_order.order_number, '5678901')

    # This test is going to check the full names of each, making sure they match
    def test_order_full_name(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.full_name, 'Michael Owen')
        self.assertEqual(second_order.full_name, 'John Smith')

    # This test is going to check the email address of each, making sure they match
    def test_order_email(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.email, 'mike@outlook.com')
        self.assertEqual(second_order.email, 'john@blueyonder.com')

    # This test is going to check the phone numbers of each, making sure they match
    def test_order_phone_number(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.phone_number, '07382422545')
        self.assertEqual(second_order.phone_number, '07833924711')

    # This test is going to check the first line of the street address of each, making sure they match
    def test_order_street_address1(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.street_address1, '21 Madeup Road')
        self.assertEqual(second_order.street_address1, '14 Somewhere Street')

    # This test is going to check the second line of the street address of each, making sure they match
    def test_order_street_address2(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.street_address2, 'Middleof Nowhere')
        self.assertEqual(second_order.street_address2, 'Random Area')

    # This test is going to check the town/city of each, making sure they match
    def test_order_town_or_city(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.town_or_city, 'Birmingham')
        self.assertEqual(second_order.town_or_city, 'Coventry')

    # This test is going to check the postcode of each, making sure they match
    def test_order_postcode(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.postcode, 'B54 3RF')
        self.assertEqual(second_order.postcode, 'C32 1RF')

    # This test is going to check the total cost of each, making sure they match
    def test_order_total_cost(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.total_cost, Decimal('49.97'))
        self.assertEqual(second_order.total_cost, Decimal('31.56'))

    # This test is going to check the original cart of each, making sure they match
    def test_order_original_cart(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.original_cart, 'a new football')
        self.assertEqual(second_order.original_cart, 'a new name')

    # This test is going to check the stripe PID of each, making sure they match
    def test_order_stripe_pid(self):
        first_order = Order.objects.get(order_number="1234567")
        second_order = Order.objects.get(order_number="5678901")
        self.assertEqual(first_order.stripe_pid, 'randomstripestuff1')
        self.assertEqual(second_order.stripe_pid, 'randomstripestuff2')


class OrderLineItemTestCase(TestCase):
    # Lets test the OrderLineItem model
    def setUp(self):
        Order.objects.create(
            full_name="Ben Smith",
            default_phone_number="07833928174",
            default_street_address1="12 Oxford Street",
            default_street_address2="Somewhere Faraway",
            default_town_or_city="Inarandom Town",
            default_postcode="B32 1TG",
        )