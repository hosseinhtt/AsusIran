from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    top_level_categories = Category.objects.filter(parent=None)
    return render(request, 'hierarchical/category_list.html', {'categories': top_level_categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # Get the hierarchical path to the selected category

    category_path = category.get_ancestors(include_self=True)

    products = Product.objects.filter(category=category)
    subcategories = category.children.all()
    context ={
            'category': category,
            'category_path': category_path,
            'products': products,
            'subcategories': subcategories,
            }
    return render(request, 'hierarchical/category_detail.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    category_path = product.category.get_ancestors(include_self=True)
    return render(request, 'hierarchical/product_detail.html', {'product': product, 'category_path': category_path})
