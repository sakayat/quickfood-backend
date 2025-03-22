from django.contrib import admin
from .models import Order, OrderItem, OrderStatus


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'status', 'created_at')
    list_filter = ('status', 'restaurant', 'created_at')
    search_fields = ('user__username', 'user__email', 'restaurant__name', 'delivery_address')
    readonly_fields = ('created_at', 'updated_at')
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price', 'total_price')
    list_filter = ('order__status', 'order__restaurant')
    search_fields = ('order__id', 'menu_item__name')
    readonly_fields = ('total_price',)
    
@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'updated_at')
    list_filter = ('status', 'updated_at')
    search_fields = ('order__id', 'status')
    readonly_fields = ('updated_at',)