from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import Manufacturer, Product
# from .factory import UserFactory
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


# class OrderTestCase(APITestCase):
#
#     def setUp(self):
#         self.create_url = reverse('orders-list')
#         self.user = UserFactory(username="emir")
#         self.user.save()
#
#         manufacturer = Manufacturer.objects.create(
#             full_name="Karl Benz",
#             description="Founder",
#             date_birth="1926-01-07"
#         )
#         self.product = Product.objects.create(name="Mercedes",
#                                     category="coupe",
#                                     price=20000,
#                                     manufacturer=manufacturer
#                                     )
#
#     def test_create_order(self):
#         data = {
#             "product": self.product.id,
#             "postal_code": 720001,
#             "user": self.user.id
#         }
#
#         self.response = self.client.post(self.create_url, data)
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class RegisterTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')

    def test_create_user(self):
        data = {
            "username": "githubuser",
            "password": "12345678",
            "email": "gihubexample@gmail.com"
        }
        self.response = self.client.post(self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_user_no_username(self):
        data = {
            "username": " ",
            "password": "123456",
            "email": "naizabekoff@gmail.com"
        }

        self.response = self.client.post(self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_mail(self):
        data = {
            "username": "Emir",
            "password": "123456",
            "email": ""
        }

        self.response = self.client.post(self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_username_long_name(self):
        data = {
            "username": "Emirverylongnaaaaaaaaaaaaaaaaaaaaaaaammmmmmeeeee",
            "password": "123456",
            "email": ""
        }

        self.response = self.client.post( self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_short_name(self):
        data = {
            "username": "Emir",
            "password": "123456",
            "email": ""
        }

        self.response = self.client.post( self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password(self):
        data = {
            "username": "Emir",
            "password": "",
            "email": "example@gmail.com"
        }
        self.response = self.client.post( self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_short(self):
        data = {
            "username": "Emir",
            "password": "1234567",
            "email": "example@gmail.com"
        }
        self.response = self.client.post( self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_long(self):
        data = {
            "username": "Emir",
            "password": "123123dfcfgvhbjkkhuiyftgdfhjkjhugyhvbjkbnkjbkjhbjkb",
            "email": "example@gmail.com"
        }
        self.response = self.client.post( self.register_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

