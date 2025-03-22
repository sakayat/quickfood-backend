from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Restaurant, Menu, Order, OrderItem, OrderStatus
from .serializers import OrderSerializer
from django.http import Http404

# Create your views here.


class CreateOrderAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        if request.user.role != "user":
            return Response(
                {"error": "Only users can create orders"},
                status=status.HTTP_403_FORBIDDEN,
            )

        required_fields = ["items", "delivery_address"]

        for field in required_fields:
            if field not in request.data:
                return Response(
                    {"error": f"{field} is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        items_data = request.data["items"]
        delivery_address = request.data["delivery_address"]
        
        items_by_restaurant = {}
        
        for item_data in items_data:
            if "menu_item_id" not in item_data:
                return Response(
                    {"error": "menu_item_id is required for each item"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                menu_item = Menu.objects.get(id=item_data["menu_item_id"])
                restaurant_id = menu_item.restaurant.id
                
                if restaurant_id not in items_by_restaurant:
                    items_by_restaurant[restaurant_id] = {
                        "restaurant": menu_item.restaurant,
                        "items": []
                    }
                
                quantity = item_data.get("quantity", 1)
                if quantity < 1:
                    return Response(
                        {"error": "Quantity must be at least 1"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                items_by_restaurant[restaurant_id]["items"].append({
                    "menu_item": menu_item,
                    "quantity": quantity,
                    "price": menu_item.price
                })
                
            except Menu.DoesNotExist:
                return Response(
                    {"error": f"Menu item with ID {item_data['menu_item_id']} not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
  
        if not items_by_restaurant:
            return Response(
                {"error": "No valid items to order"},
                status=status.HTTP_400_BAD_REQUEST,
            )
 
        created_orders = []
        
        for restaurant_id, restaurant_data in items_by_restaurant.items():
            restaurant = restaurant_data["restaurant"]
            order_items = restaurant_data["items"]
  
            total_amount = sum(item["price"] * item["quantity"] for item in order_items)

            order = Order.objects.create(
                user=request.user,
                restaurant=restaurant,
                status="pending",
                delivery_address=delivery_address,
            )
            
            for item_data in order_items:
                OrderItem.objects.create(
                    order=order,
                    menu_item=item_data["menu_item"],
                    quantity=item_data["quantity"],
                    price=item_data["price"],
                )
            

            OrderStatus.objects.create(order=order, status="pending")
            
            created_orders.append({
                "order_id": order.id,
                "restaurant": {"id": restaurant.id, "name": restaurant.name},
                "total_amount": total_amount,
                "status": order.status,
                "delivery_address": order.delivery_address,
                "created_at": order.created_at,
            })
        
        return Response(
            {"message": "Orders created successfully", "orders": created_orders},
            status=status.HTTP_201_CREATED
        )


class UserOrderListAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        user = request.user

        orders = Order.objects.filter(user=user)

        sort_by = request.query_params.get("sort_by", "-created_at")
        orders = orders.order_by(sort_by)

        serializer = OrderSerializer(orders, many=True)

        return Response(
            {"count": orders.count(), "orders": serializer.data},
            status=status.HTTP_200_OK,
        )


class UpdateOrderStatusAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, order_id):
        user = self.request.user
        try:
            if user.role == "restaurant_owner":
                order = Order.objects.get(id=order_id, restaurant__owner=user)
            else:
                return Response(
                    {"detail": "You don't have permission to update the order status"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            return order
        except Order.DoesNotExist:
            return Response(
                {"detail": f"order id not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, id):

        order = self.get_object(id)

        if isinstance(order, Response):
            return order

        new_status = request.data.get("status")

        if not new_status:
            return Response(
                {"detail": "Status field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order.status = new_status
        order.save()

        OrderStatus.objects.create(order=order, status=new_status)

        serializer = OrderSerializer(order)

        return Response({"message": f"Order status updated", "order": serializer.data})


class RestaurantOrdersAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        if request.user.role != "restaurant_owner":
            return Response(
                {"error": "restaurant owners can access"},
                status=status.HTTP_403_FORBIDDEN,
            )
            
        try:
            restaurant = Restaurant.objects.get(owner=request.user)
        except Restaurant.DoesNotExist:
            return Response(
                {"error": "You don't have a restaurant"},
                status=status.HTTP_404_NOT_FOUND,
            )
            
        orders = Order.objects.filter(restaurant=restaurant).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)