from django.urls import path, include
from .views import RegisterView, LoginApiView, UserProfileView, UpdateProfileView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("update-profile/", UpdateProfileView.as_view(), name="update-profile"),
]
