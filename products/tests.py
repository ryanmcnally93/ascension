from django.test import TestCase
from .models import Category, Product


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="electric_guitars", friendly_name="Electric Guitars")
        Category.objects.create(name="drum_kits", friendly_name="Drum Kits")

    def test_category_friendly_name(self):
        electric_guitars = Category.objects.get(name="electric_guitars")
        drum_kits = Category.objects.get(name="drum_kits")
        self.assertEqual(electric_guitars.friendly_name, 'Electric Guitars')
        self.assertEqual(drum_kits.friendly_name, 'Drum Kits')
