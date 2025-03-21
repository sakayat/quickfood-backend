from rest_framework import serializers
from .models import Order, OrderItem, OrderStatus
from .models import Order, OrderItem, OrderStatus
from restaurants.serializers import MenuSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='menu_item.name')
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["name", "quantity", "price", "total_price"]
        read_only_fields = ["price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "status",
            "delivery_address",
            "items",
        ]

