from django.urls import path
from .views import CreateRestaurantAPIView, UpdateRestaurantAPIView

urlpatterns = [
    path(
        "create-restaurant/",
        CreateRestaurantAPIView.as_view(),
        name="create-restaurant",
    ),
    path(
        "update-restaurant/",
        UpdateRestaurantAPIView.as_view(),
        name="update-restaurant",
    ),
]
