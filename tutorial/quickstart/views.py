from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework.decorators import api_view

class BlogViews(views.APIView): # APIView - often used for regis/auth

    def get(self, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

class BlogGenerics(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogViewsets(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostViews(views.APIView):
    def get(self, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostGenerics(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
