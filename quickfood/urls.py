from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # users endpoints
    path('api/users/', include('users.urls')),
    # restaurant endpoints
    path('api/', include('restaurants.urls')),
    # orders endpoints
    path('api/', include('orders.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)