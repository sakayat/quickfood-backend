from django.contrib import admin
from .models import Restaurant, Menu


# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "location", "created_at")
    list_filter = ("location", "created_at")
    search_fields = ("name", "description", "location")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "price", "created_at")
    list_filter = ("restaurant", "created_at")
    search_fields = ("name", "description")
    readonly_fields = ("created_at", "updated_at")
