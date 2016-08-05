from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(max_length=1000)
    brand_name = models.CharField(max_length=20)


