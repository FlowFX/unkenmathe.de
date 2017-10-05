"""ModelFactory for Sheets."""
from factory.django import DjangoModelFactory
from factory import post_generation, SubFactory

from um.core.factories import UserFactory

from .models import Sheet



class SheetFactory(DjangoModelFactory):
    """Model factory for the Sheet model."""

    class Meta:  # noqa: D101
        model = Sheet

    author = SubFactory(UserFactory)

    @post_generation
    def exercises(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:  # pragma: no branch
            # A list of groups were passed in, use them
            for exercise in extracted:
                self.exercises.add(exercise)
