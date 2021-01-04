from rest_framework import serializers
from .models import *




class PostSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'description', 'date_created', 'posts']

class BlogForAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'date_created']

class AuthorSerializer(serializers.ModelSerializer):
    blogs = BlogForAuthorSerializer(many=True)
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'phone', 'birth_date', 'email', 'gender', 'blogs']

class UserSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'author']

    def create(self, validate_data):
        password = validate_data['password']
        author_data = validate_data.pop('author')
        user = User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        Author.objects.create(user=user, **author_data)
        return user