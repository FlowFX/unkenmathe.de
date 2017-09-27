"""Unit tests for the forms."""
from um.core import factories
from um.exercises import forms

import pytest

from authtools.models import User


class TestExerciseForms:

    TESTPARAMS_EXERCISE = [
        # is original
        ('$5x + 4 = 20$.', 'cc-by', True, None, '', True),
        ('$5x + 4 = 20$.', 'cc-by-sa', True, None, '', True),
        ('', 'cc-by', True, None, '', False),  # text is required
        ('$5x + 4 = 20$.', '', True, None, '', False),  # license is required
        ('$5x + 4 = 20$.', 'cc-by-XX', True, None, '', False),  # license is one of cc-by|cc-by-sa
        ('$5x + 4 = 20$.', 'cc-by', True, True, 'http://dings.com', True),  # ignores a given source
        # is NOT original
        ('$5x + 4 = 20$.', 'cc-by', False, True, 'https://de.serlo.org/mathe/xxx', True),
        ('$5x + 4 = 20$.', 'cc-by', False, True, '', False),  # if original_author exists, source URL is required
    ]

    @pytest.mark.parametrize('text, license, is_original, original_author, source_url, validity', TESTPARAMS_EXERCISE)
    def test_exercise_form(self, db, text, license, is_original, original_author, source_url, validity):
        """Unit test the Exercise Form."""
        # GIVEN a user and form data
        users = factories.UserFactory.create_batch(2)

        data={
            'text': text,
            'license': license,
            'is_original': is_original,
        }
        if original_author:
            data['original_author'] = users[0].id
            data['source_url'] = source_url

        # WHEN submitting the form as the original author
        form = forms.ExerciseForm(
            data=data,
            user=users[1]
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity
