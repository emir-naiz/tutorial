from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    genders = (
        ('female', 'female'),
        ('mael', 'male')
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(choices=genders, max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='blogs')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, related_name='posts')
    title = models.CharField(max_length=20)
    description = models.TextField()
    file = models.FileField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



