# shop/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class ProductFeature(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    features = models.ManyToManyField(ProductFeature, through='ProductFeatureValue')

class ProductFeatureValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.ForeignKey(ProductFeature, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
