from django.urls import path
from . import views

urlpatterns = [
    path('category', views.list_category),
    path('category/<int:pk>/detail', views.category_detail),
    path('product',views.list_product),
    path('product/<int:pk>/detail', views.product_detail)
]