from django.urls import path
from .views import (
    CreateOrderAPIView,
    UserOrderListAPIView,
    UpdateOrderStatusAPIView,
    RestaurantOrdersAPIView,
)

urlpatterns = [
    path("create-order/", CreateOrderAPIView.as_view(), name="create-order"),
    path("my-orders/", UserOrderListAPIView.as_view(), name="user-orders"),
    path(
        "update-order-status/<int:id>/",
        UpdateOrderStatusAPIView.as_view(),
        name="user-orders",
    ),
    path(
        "user-orders/",
        RestaurantOrdersAPIView.as_view(),
        name="restaurant-orders",
    ),
]
