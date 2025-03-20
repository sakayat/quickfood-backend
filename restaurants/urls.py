from django.urls import path
from .views import (
    CreateRestaurantAPIView,
    UpdateRestaurantAPIView,
    CreateMenuAPIView,
    UpdateMenuAPIView,
    RestaurantDetailAPIView,
)

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
    path("menu-update/<int:menu_id>/", UpdateMenuAPIView.as_view(), name="menu-update"),
    path(
        "restaurant/<int:restaurant_id>/",
        RestaurantDetailAPIView.as_view(),
        name="restaurant-detail",
    ),
]
