from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "location", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class MenuSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(source="restaurant.id", read_only=True)

    class Meta:
        model = Menu
        fields = [
            "id",
            "name",
            "description",
            "price",
            "restaurant_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["restaurant_id", "created_at", "updated_at"]


class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)
    owner_name = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "owner",
            "name",
            "description",
            "location",
            "owner_name",
            "menus",
        ]
        read_only_fields = ["owner"]


class RestaurantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "location"]
