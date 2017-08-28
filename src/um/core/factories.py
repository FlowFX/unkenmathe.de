"""ModelFactory for core models."""
from factory.django import DjangoModelFactory

from django.conf import settings

from factory import Faker as faker


class UserFactory(DjangoModelFactory):
    """Model factory for the User model."""

    class Meta:  # noqa: D101
        model = settings.AUTH_USER_MODEL

    email = faker('email')
    name = faker('name')
