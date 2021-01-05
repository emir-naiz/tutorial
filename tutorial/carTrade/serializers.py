from django.contrib.auth.models import User
from rest_framework import serializers, generics, viewsets
from .models import Product, Manufacturer, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'category', 'price', 'manufacturer']

class ManufacturerSerializerDetail(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Manufacturer
        fields = ['id', 'full_name', 'description', 'date_birth', 'products']

class ManufacturerSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'full_name', 'date_birth']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    class Meta:
        model = Order
        fields = ['id', 'product', 'date_created', 'status', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'username', 'email', 'password']
