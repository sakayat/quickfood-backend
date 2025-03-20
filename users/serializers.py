from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop("password2")

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            role="user",
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "role",
            "profile_image",
        ]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User 
        fields = ["first_name", "last_name", "phone_number", "address", "profile_image"]
        
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.address = validated_data.get("address", instance.address)
        
        if "profile_image" in validated_data:
            instance.profile_image = validated_data.get("profile_image")
        
        instance.save()
        return instance
