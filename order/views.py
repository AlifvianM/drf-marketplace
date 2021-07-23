from django.shortcuts import render
from .serializer import OrderItemSerializer, OrderSerializer, PaymentSerializer
from .models import Order, Payment, OrderItem

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.

@cache_page(60 * 30)
@api_view(['GET', 'POST'])
def list_payment(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializers = PaymentSerializer(payments, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = PaymentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk):
    try:
        obj = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PaymentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@cache_page(60 * 30)
@api_view(['GET', 'POST'])
def list_orderitem(request):
    if request.method == 'GET':
        orders = OrderItem.objects.all()
        serializers = OrderItemSerializer(orders, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = OrderItemSerializer(data = request.data)
        if serializers.is_valid(raise_exception = True):
            order,status_order = Order.objects.get_or_create(address='', phone='')
            serializers.save(order = order)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderitem_detail(request, pk):
    try:
        obj = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderItem(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        cache.clear()
        serializer = OrderItem(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def list_order(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializers = OrderSerializer(orders, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = OrderSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        obj = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        cache.clear()
        serializer = OrderSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cache.clear()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
