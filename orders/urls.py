from django.urls import path
from .views import CreateOrderAPIView, UserOrderListAPIView, UpdateOrderStatusAPIView

urlpatterns = [
    path("create-order/", CreateOrderAPIView.as_view(), name="create-order"),
    path("my-orders/", UserOrderListAPIView.as_view(), name="user-orders"),
    path("<int:id>/status/", UpdateOrderStatusAPIView.as_view(), name="user-orders"),
    
]
