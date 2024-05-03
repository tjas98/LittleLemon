from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    def test(self):
        print("TEST")
    def test_add_item(self):
        item = Menu.objects.create(title="Gelato", price=1.20, inventory = 100)
        self.assertEqual(item, "Gelato : 1.20")