from rest_framework import serializers
from .models import Restaurant


class RestaurantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "location", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
