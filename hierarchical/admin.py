from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)