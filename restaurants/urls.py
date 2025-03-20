from django.urls import path
from .views import CreateRestaurantAPIView, UpdateRestaurantAPIView, CreateMenuAPIView

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
    path("create-menus/", CreateMenuAPIView.as_view(), name="create-menus"),
]
