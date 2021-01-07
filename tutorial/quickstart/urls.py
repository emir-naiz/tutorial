from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register('blogs', BlogViewsets)
router.register('posts', PostViewsets)
# router.register(r'register', UserViewsets)
router.register(r'authors', AuthorViewset)

urlpatterns = [
    path('views/', BlogViews.as_view()),
    path('generics/', BlogGenerics.as_view()),
    path('posts/', PostViews.as_view()),
    path('generics_post/', PostGenerics.as_view()),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)