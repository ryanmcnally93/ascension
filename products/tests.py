from django.test import TestCase
from .models import Category, Product
from decimal import *


class CategoryTestCase(TestCase):
    # Lets first test the Category model
    # Here we are creating two new categories with names and friendly names
    def setUp(self):
        Category.objects.create(name="electric_guitars", friendly_name="Electric Guitars")
        Category.objects.create(name="drum_kits", friendly_name="Drum Kits")

    # This test is going to check the friendly names of each, making sure they match
    def test_category_friendly_name(self):
        electric_guitars = Category.objects.get(name="electric_guitars")
        drum_kits = Category.objects.get(name="drum_kits")
        self.assertEqual(electric_guitars.friendly_name, 'Electric Guitars')
        self.assertEqual(drum_kits.friendly_name, 'Drum Kits')

    # This test is going to check the names of each, making sure they match
    def test_category_name(self):
        electric_guitars = Category.objects.get(friendly_name="Electric Guitars")
        drum_kits = Category.objects.get(friendly_name="Drum Kits")
        self.assertEqual(electric_guitars.name, 'electric_guitars')
        self.assertEqual(drum_kits.name, 'drum_kits')


class ProductTestCase(TestCase):
    # Now let's test the more complicated Product Model

    def setUp(self):
        Product.objects.create(
            sku="newproduct1",
            name="Test Guitar Strings",
            description="These guitar strings are a test item!",
            price="99.99",
            amount_sold="0",
            amount_of_reviews="0",
            rating="2.0",
            main_image="testone.jpg",
            image="testtwo.jpg",
            image_2="testthree.jpg",
            image_3="testfour.jpg",
            is_hire_room="False",
            is_offers_item="False",
            )
        Product.objects.create(
            sku="newproduct2",
            name="Test Capo",
            description="This Capo is a test item!",
            price="9.99",
            amount_sold="5",
            amount_of_reviews="2",
            rating="2.0",
            main_image="testcapoone.jpg",
            image="testcapotwo.jpg",
            image_2="testcapothree.jpg",
            image_3="testcapofour.jpg",
            is_hire_room="False",
            is_offers_item="True",
            striked_price="19.99"
            )
        Product.objects.create(
            sku="newsessionproduct",
            name="Test Session",
            description="This Session is a test item!",
            price="29.99",
            amount_sold="15",
            amount_of_reviews="6",
            rating="4.0",
            main_image="testsessionone.jpg",
            image="testsessiontwo.jpg",
            image_2="testsessionthree.jpg",
            image_3="testsessionfour.jpg",
            is_hire_room="True",
            is_offers_item="False",
            )

    # This test is going to check the sku of each, making sure they match
    def test_product_sku(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.sku, 'newproduct1')
        self.assertEqual(capo_item.sku, 'newproduct2')
        self.assertEqual(session_item.sku, 'newsessionproduct')

    # This test is going to check the description of each, making sure they match
    def test_product_description(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.description, 'These guitar strings are a test item!')
        self.assertEqual(capo_item.description, 'This Capo is a test item!')
        self.assertEqual(session_item.description, 'This Session is a test item!')

    # This test is going to check the price of each, making sure they match
    def test_product_price(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.price, Decimal('99.99'))
        self.assertEqual(capo_item.price, Decimal('9.99'))
        self.assertEqual(session_item.price, Decimal('29.99'))

    # This test is going to check the amount sold of each, making sure they match
    def test_product_amount_sold(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.amount_sold, 0)
        self.assertEqual(capo_item.amount_sold, 5)
        self.assertEqual(session_item.amount_sold, 15)

    # This test is going to check the amount of reviews for each, making sure they match
    def test_product_amount_of_reviews(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.amount_of_reviews, 0)
        self.assertEqual(capo_item.amount_of_reviews, 2)
        self.assertEqual(session_item.amount_of_reviews, 6)

    # This test is going to check the rating of each, making sure they match
    def test_product_rating(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.rating, 2.0)
        self.assertEqual(capo_item.rating, 2.0)
        self.assertEqual(session_item.rating, 4.0)

    # This test is going to check the main image of each, making sure they match
    def test_product_main_image(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.main_image, 'testone.jpg')
        self.assertEqual(capo_item.main_image, 'testcapoone.jpg')
        self.assertEqual(session_item.main_image, 'testsessionone.jpg')

    # This test is going to check the first image of each, making sure they match
    def test_product_image(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.image, 'testtwo.jpg')
        self.assertEqual(capo_item.image, 'testcapotwo.jpg')
        self.assertEqual(session_item.image, 'testsessiontwo.jpg')

    # This test is going to check the second image of each, making sure they match
    def test_product_image_2(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.image_2, 'testthree.jpg')
        self.assertEqual(capo_item.image_2, 'testcapothree.jpg')
        self.assertEqual(session_item.image_2, 'testsessionthree.jpg')

    # This test is going to check the third image of each, making sure they match
    def test_product_image_3(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.image_3, 'testfour.jpg')
        self.assertEqual(capo_item.image_3, 'testcapofour.jpg')
        self.assertEqual(session_item.image_3, 'testsessionfour.jpg')

    # This test is going to check the amount sold of each, making sure they match
    def test_product_is_hire_room(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.is_hire_room, False)
        self.assertEqual(capo_item.is_hire_room, False)
        self.assertEqual(session_item.is_hire_room, True)

    # This test is going to check the amount sold of each, making sure they match
    def test_product_is_offers_item(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.is_offers_item, False)
        self.assertEqual(capo_item.is_offers_item, True)
        self.assertEqual(session_item.is_offers_item, False)

    # This test is going to check the amount sold of each, making sure they match
    def test_product_striked_price(self):
        guitar_strings_item = Product.objects.get(name="Test Guitar Strings")
        capo_item = Product.objects.get(name="Test Capo")
        session_item = Product.objects.get(name="Test Session")
        self.assertEqual(guitar_strings_item.striked_price, None)
        self.assertEqual(capo_item.striked_price, Decimal('19.99'))
        self.assertEqual(session_item.striked_price, None)
