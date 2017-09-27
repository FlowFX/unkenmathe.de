"""Test fixtures."""
from django.contrib.auth.models import AnonymousUser

from um.core.factories import UserFactory
from um.exercises.factories import ExerciseFactory

import pytest


@pytest.fixture(scope="session")
def users():
    users = {
        'anonymous': AnonymousUser(),
        'authenticated': UserFactory.build(),
        'staff': UserFactory.build(is_staff=True)
    }
    users['author'] = users['authenticated']

    return users


@pytest.fixture(scope="module")
def exercises():
    exercises = ExerciseFactory.build_batch(2)

    for ex in exercises:
        ex.render_html()

    return exercises
