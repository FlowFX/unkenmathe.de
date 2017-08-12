"""ModelFactory for Exercises."""
from factory.django import DjangoModelFactory

from .models import Exercise

from factory import Faker as faker


class ExerciseFactory(DjangoModelFactory):
    """Model factory for the Exercise model."""

    class Meta:
        model = Exercise

    text = faker('sentence')
