from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view

# class ProductViews(views.APIView): # APIView - often used for regis/auth
#
#     def get(self, *args, **kwargs):
#         blogs = Product.objects.all()
#         serializer = ProductSerializer(blogs, many=True)
#         return Response(serializer.data)
#
# class ProductGenerics(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ManufacturerViewsets(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializerDetail

    def list(self, request, *args, **kwargs):
        self.serializer_class = ManufacturerSerializerList
        return super().list(request, *args, **kwargs)

class OrderViewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

