from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # users endpoints
    path('api/users/', include('users.urls')),
    # restaurant endpoints
    path('api/', include('restaurants.urls')),
    # orders endpoints
    path('api/', include('orders.urls')),
]
