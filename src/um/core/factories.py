"""ModelFactory for core models."""
from factory.django import DjangoModelFactory

from authtools.models import User

from factory import Faker as faker


class UserFactory(DjangoModelFactory):
    """Model factory for the User model."""

    class Meta:
        model = User

    email = faker('email')
    name = faker('name')
