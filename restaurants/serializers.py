from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "location", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')