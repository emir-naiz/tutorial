import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

User = get_user_model()

class UserFactory(factory.django,DjangoModelFactory):
    class Meta:
        model = User