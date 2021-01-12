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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'product', 'date_created', 'status', 'user', 'postal_code']

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=5)
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(max_length=16, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

