"""ModelFactory for Exercises."""
from factory.django import DjangoModelFactory

from um.core.factories import UserFactory
from .models import Exercise, ExerciseExample

from factory import Faker as faker
from factory import SubFactory


class ExerciseFactory(DjangoModelFactory):
    """Model factory for the Exercise model."""

    class Meta:  # noqa: D101
        model = Exercise

    author = SubFactory(UserFactory)
    text = faker('sentence')
    text_html = ''
    text_tex = ''


class ExerciseExampleFactory(DjangoModelFactory):
    """Model factory for Exercise examples."""

    class Meta:  # noqa: D101
        model = ExerciseExample

    title = faker('sentence')
    description = faker('paragraph')

    exercise = SubFactory(ExerciseFactory)
