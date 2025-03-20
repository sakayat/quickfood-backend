from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import RestaurantCreateSerializer, MenuSerializer
from .models import Restaurant

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


class UpdateRestaurantAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        if self.request.user.role != "restaurant_owner":
            return Response(
                {"error": "Only restaurant owners can create restaurants"},
                status=status.HTTP_403_FORBIDDEN,
            )
        restaurant = Restaurant.objects.get(owner=self.request.user)
        return restaurant

    def put(self, request):
        restaurant = self.get_object()
        serializer = RestaurantCreateSerializer(
            restaurant, data=request.data, partial=True
        )

        if serializer.is_valid():
            restaurant = serializer.save()

            response_data = {
                "id": restaurant.id,
                "owner": restaurant.owner.id,
                "name": restaurant.name,
                "description": restaurant.description,
                "location": restaurant.location,
            }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateMenuAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if request.user.role != "restaurant_owner":
            return Response(
                {"error": "Only restaurant owners can add menu items"},
                status=status.HTTP_403_FORBIDDEN,
            )

        restaurant = Restaurant.objects.get(owner=request.user)

        serializer = MenuSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            menu_item = serializer.save(restaurant=restaurant)
            return Response(
                MenuSerializer(menu_item).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

