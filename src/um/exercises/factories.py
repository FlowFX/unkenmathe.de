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

    slug = faker('password', length=5, special_chars=False, digits=True, upper_case=False, lower_case=False)
    published = False

    author = SubFactory(UserFactory)
    original_author = SubFactory(UserFactory)

    text = faker('sentence')
    text_html = ''
    text_tex = ''

    is_original = True


class ExerciseExampleFactory(DjangoModelFactory):
    """Model factory for Exercise examples."""

    class Meta:  # noqa: D101
        model = ExerciseExample

    title = faker('sentence')
    description = faker('paragraph')

    exercise = SubFactory(ExerciseFactory)
