"""Test fixtures."""
from django.contrib.auth.models import AnonymousUser

from um.core.factories import UserFactory

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
