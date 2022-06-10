import json
from django.db import models
from rest_framework import serializers

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.TextField(default='')
    masterCategory = models.TextField(default='')
    subCategory = models.TextField(default='')
    articleType = models.TextField(default='')
    baseColour = models.TextField(default='')
    season = models.TextField(default='')
    year = models.IntegerField(default=0)
    usage = models.TextField(default='')
    productDisplayName = models.TextField(default='')
    price = models.IntegerField(default=0)
    link = models.TextField(default='')

    def __str__(self):
        return self.productDisplayName

class Footwear(Product):
    stock38 = models.IntegerField(default=0)
    stock39 = models.IntegerField(default=0)
    stock40 = models.IntegerField(default=0)
    stock41 = models.IntegerField(default=0)
    stock42 = models.IntegerField(default=0)
    stock43 = models.IntegerField(default=0)
    stock44 = models.IntegerField(default=0)
    stock45 = models.IntegerField(default=0)
    
class Apparel(Product):
    stocks = models.IntegerField(default=0)
    stockm = models.IntegerField(default=0)
    stockl = models.IntegerField(default=0)
    stockxl = models.IntegerField(default=0)
    stockxxl = models.IntegerField(default=0)

