from itertools import product

from django.test import TestCase

# Create your tests here.
from .models import Product
#
# TYPE_CHOICES = (
#     ('L', 'Laptop'),
#     ('D', 'Desktop'),
# )
# type = models.CharField(max_length=1, choices=TYPE_CHOICES)
# productName = models.CharField(max_length=200)
# slug = models.SlugField(unique=True)
# category = models.CharField(max_length=200)
# image = StdImageField(upload_to='%Y/%m/%d/')
# price = models.IntegerField()
# stock = models.IntegerField()
# description = models.TextField(max_length=1000)
# brand_name = models.CharField(max_length=20)
class ProductMethodTests(TestCase):

    def setUp(self):
        Product.objects.create(type='L',
                               productName="Azad Product",
                               category='Azad',
                               price=12,
                               slug='www.example.com/article/The%2046%20Year%20Old%20Virgin',
                               description="This is very nice product",
                               brand_name="Jamil",
                               stock=12
                               )

    def test_descriptions(self):

        azad_product = Product.objects.get(productName="Azad Product")

        self.assertEqual(azad_product.description, "This is very nice product")

