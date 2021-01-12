from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('products', ProductViewsets, basename='products')
router.register('manufacturer/products', ManufacturerViewsets)
router.register('orders', OrderViewsets, basename='order')

urlpatterns = [
                  path('', include(router.urls)),
                  path('register/', SignUp.as_view(), name='register'),
                  path('login/',csrf_exempt(LoginView.as_view())),
                  path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)