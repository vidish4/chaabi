from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Product(models.Model):
    index = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    # sale_price = models.IntegerField()
    sale_price = models.CharField(max_length=100)
    # market_price = models.IntegerField()
    market_price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    # rating = models.FloatField()
    rating = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    vector = models.CharField(max_length=2000)