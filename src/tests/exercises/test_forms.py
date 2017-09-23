"""Unit tests for the forms."""
from um.core import factories
from um.exercises import forms

import pytest


class TestExerciseForms:

    TESTPARAMS_EXERCISE = [
        ('$5x + 4 = 20$.', 'cc-by',    True),
        ('$5x + 4 = 20$.', 'cc-by-sa', True),
        ('$5x + 4 = 20$.', 'cc-by-nd', True),
        ('',               'cc-by',    False),  # text is required
        ('$5x + 4 = 20$.', '',         False),  # license is required
        ('$5x + 4 = 20$.', 'cc-by-XX', False),  # license is one of cc-by|cc-by-sa|cc-by-na
    ]

    @pytest.mark.parametrize('text, license, validity', TESTPARAMS_EXERCISE)
    def test_exercise_form(self, text, license, validity):
        """Unit test the Exercise Form."""
        # WHEN submitting the form with data
        form = forms.ExerciseForm(
            data={
                'text': text,
                'license': license,
                },
            user=factories.UserFactory.build()
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity
