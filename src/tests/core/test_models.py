"""Test core models."""
from um.core import factories


class TestUserModel:

    def test_can_build_new_user(self):
        """Check if UserFactory works."""
        factories.UserFactory.build()
