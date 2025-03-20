from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import RestaurantCreateSerializer

# Create your views here.


class CreateRestaurantAPIView(APIView):

    def post(self, request):
        if request.user.role != "restaurant_owner":
            return Response(
                {"error": "Only restaurant owners can create restaurants"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = RestaurantCreateSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            restaurant = serializer.save(owner=request.user)

            response_data = {
                "id": restaurant.id,
                "owner": restaurant.owner.id,
                "name": restaurant.name,
                "description": restaurant.description,
                "location": restaurant.location,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
