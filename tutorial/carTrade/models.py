import cars as cars
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    cars = (
        ('sedan', 'sedan'),
        ('coupe', 'coupe'),
        ('sportscar', 'sportscar'),
        ('minivan', 'minivan'),
        ('pickup truck', 'pickup truck'),
        ('convertible', 'convertible')
    )
    image = models.ImageField()
    name = models.CharField(max_length=50, verbose_name='Название авто')
    category = models.CharField(max_length=20, choices=cars, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True, verbose_name='Производитель',
                                     related_name='products')

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Авто'

class Manufacturer(models.Model):
    full_name = models.CharField(max_length=200)
    description = models.TextField()
    date_birth = models.DateField()

    class Meta:
        verbose_name = 'Проиводитель'
        verbose_name_plural = 'Проиводитель'


class Order(models.Model):
    statuses = (
        ('Not delivered', 'Not delivered'),
        ('In process', 'In process'),
        ('Delivered', 'Delivered')
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='products')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=statuses, default='New order')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postal_code = models.IntegerField()

    def str(self):
        return self.product.name + ' ' + self.user.first_name + ' ' + str(self.postal_code)

    class Meta:
        verbose_name="Заказы"
        verbose_name_plural="Заказы"
