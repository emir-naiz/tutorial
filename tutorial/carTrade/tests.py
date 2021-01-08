from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import Manufacturer
from rest_framework.test import force_authenticate
# Create your tests here.

class ProductTestCase(APITestCase):

    def setUp(self):
        self.create_url = reverse('products-list')
        User.objects.create(username="emir1", password="emir12345")
        Manufacturer.objects.create(full_name="Karl Benz",
                                    description="Founder",
                                    date_birth="1926-01-07"
                                    )


    def test_create_product(self):
        data = {
            "name": "MercedesSLS500",
            "category": "sportscar",
            "price": 180000,
            "manufacturer": 1
        }
        self.response = self.client.post(path=self.create_url, data=data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_tooLong_product_name(self):
        data = {
            "name": "ChacarronMakarronLagavillywowYippieYowYippieYeah",
            "category": "sportcar",
            "price": 200000,
            "manufacturer": 1
        }
        self.response = self.client.post(path=self.create_url, data=data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)