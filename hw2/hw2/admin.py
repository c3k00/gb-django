from django.contrib import admin
from .models import Client, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)