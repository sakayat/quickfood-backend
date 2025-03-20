from django.urls import path, include
from .views import RegisterView, LoginApiView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),
]
