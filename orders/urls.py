from django.urls import path
from .views import CreateOrderAPIView, UserOrderListAPIView

urlpatterns = [
    path("create-order/", CreateOrderAPIView.as_view(), name="create-order"),
    path('my-orders/', UserOrderListAPIView.as_view(), name='user-orders'),
]
