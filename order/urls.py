from django.urls import path
from . import views

urlpatterns = [
    path('payment', views.list_payment),
    path('payment/<int:pk>/detail',views.payment_detail),
    path('order', views.list_order),
    path('order/<int:pk>/detail',views.order_detail),
    path('orderitem', views.list_orderitem)
]