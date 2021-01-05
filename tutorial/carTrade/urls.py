from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewsets)
router.register('manufacturer/products', ManufacturerViewsets)
router.register('orders', OrderViewsets)

urlpatterns = [
    # path('views/', ProductViews.as_view()),
    # path('generics/', ProductGenerics.as_view()),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)