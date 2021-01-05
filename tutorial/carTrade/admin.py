from django.contrib import admin
from .models import Product, Manufacturer, Order


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'manufacturer']

admin.site.register(Product, ProductAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['full_name']

admin.site.register(Manufacturer, ManufacturerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product']

admin.site.register(Order, OrderAdmin)