from django.urls import path
from .views import CreateRestaurantAPIView

urlpatterns = [
    path(
        "create-restaurant/",
        CreateRestaurantAPIView.as_view(),
        name="create-restaurant",
    ),
]
