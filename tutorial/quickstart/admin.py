from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'description', 'date_created']

admin.site.register(Blog, BlogAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'description', 'date_created']

admin.site.register(Post, PostAdmin)
