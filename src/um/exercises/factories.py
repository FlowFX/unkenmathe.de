"""ModelFactory for Exercises."""
from factory.django import DjangoModelFactory

from um.core.factories import UserFactory
from .models import Exercise

from factory import Faker as faker
from factory import SubFactory


class ExerciseFactory(DjangoModelFactory):
    """Model factory for the Exercise model."""

    class Meta:
        model = Exercise

    author = SubFactory(UserFactory)
    text = faker('sentence')
    text_html = ''
    text_tex = ''
