from django.urls import path, include

from carTrade.views import SignUp
from .views import DocumentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('documents', DocumentsViewSet, basename='documents')

urlpatterns = [
                  path('', include(router.urls)),
                  path('register/', SignUp.as_view(), name='register'),
              ]