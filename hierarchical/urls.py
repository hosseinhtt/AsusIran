from django.urls import path
from . import views

app_name='hierarchical'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]