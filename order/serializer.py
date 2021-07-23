from rest_framework import  serializers
from .models import Payment, Order, OrderItem

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     order = Order.objects.create(**validated_data)

    #     for item_data in items_data:
    #         OrderItem.objects.create(order=order, **item_data)
            
    #     return order