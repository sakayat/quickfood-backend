from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import (
    RestaurantCreateSerializer,
    MenuSerializer,
    RestaurantSerializer,
)
from .models import Restaurant, Menu
from django.http import Http404

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


class UpdateMenuAPIView(APIView):

    def get_object(self, menu_id):
        if self.request.user.role != "restaurant_owner":
            return Response(
                {"error": "Only restaurant owners can update menu items"},
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            restaurant = Restaurant.objects.get(owner=self.request.user)
        except Restaurant.DoesNotExist:
            raise Http404("You don't have any restaurant to update")

        try:
            menu = Menu.objects.get(id=menu_id, restaurant=restaurant)
            return menu
        except Menu.DoesNotExist:
            raise Http404(f"Menu item with id {menu_id} not found in your restaurant")

    def put(self, request, menu_id):
        menu = self.get_object(menu_id)
        serializer = MenuSerializer(menu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPIView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, restaurant_id):

        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response(
                {"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)
