# shop/admin.py
from django.contrib import admin
from .models import Category, Product, ProductFeature

class ProductFeatureInline(admin.TabularInline):
    model = Product.features.through

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline]

admin.site.register(Category)
admin.site.register(ProductFeature)
admin.site.register(Product, ProductAdmin)
