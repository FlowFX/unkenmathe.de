"""Unit tests for the forms."""
from um.core import factories
from um.exercises import forms

import pytest


class TestExerciseForms:

    TESTPARAMS_IS_ORIGINAL = [
        ('$5x + 4 = 20$.', 'cc-by', True),
        ('$5x + 4 = 20$.', 'cc-by-sa', True),
        ('', 'cc-by', False),  # text is required
        ('$5x + 4 = 20$.', '', False),  # license is required
        ('$5x + 4 = 20$.', 'cc-by-XX', False),  # license is one of cc-by|cc-by-sa
    ]

    @pytest.mark.parametrize('text, license, validity', TESTPARAMS_IS_ORIGINAL)
    def test_exercise_form_if_is_original(self, db, text, license, validity):
        """Unit test the Exercise Form."""
        # GIVEN a user and form data
        data={
            'text': text,
            'license': license,
            'is_original': True,
            'original_author': None,
            'source_url': '',
            'changes': '',
        }

        # WHEN submitting the form as the original author
        form = forms.ExerciseForm(
            data=data,
            user=factories.UserFactory.create(),
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity

    TESTPARAMS_IS_SOURCED = [
        ('https://de.serlo.org/mathe/xxx', 'none', True),
        ('', 'none', False),  # if original_author exists, source URL is required
        ('https://de.serlo.org/mathe/xxx', '', False),  # info about changes is required
        ('https://de.serlo.org/mathe/xxx', 'xyz', False),  # only one of 'none'|???   is allowed
    ]

    @pytest.mark.parametrize('source_url, changes, validity', TESTPARAMS_IS_SOURCED)
    def test_exercise_form_if_sourced(self, db, source_url, changes, validity):
        """Unit test the Exercise Form."""
        # GIVEN a user and form data
        users = factories.UserFactory.create_batch(2)

        data={
            'text': '$5x + 4 = 20$.',
            'license': 'cc-by',
            'is_original': False,
            'original_author': users[0].id,
            'source_url': source_url,
            'changes': changes,
        }

        # WHEN submitting the form as the original author
        form = forms.ExerciseForm(
            data=data,
            user=users[1],
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity
