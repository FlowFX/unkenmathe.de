"""Unit tests for the forms."""
from um.core import factories
from um.exercises import forms

import pytest


class TestExerciseForms:

    TESTPARAMS_EXERCISE = [
        ('Dies ist eine einfach Aufgabe: $5x + 4 = 20$.', True),
    ]

    @pytest.mark.parametrize('text, validity', TESTPARAMS_EXERCISE)
    def test_exercise_form(self, text, validity):
        """Unit test the Exercise Form."""
        # WHEN submitting the form with data
        form = forms.ExerciseForm(
            data={'text': text},
            user=factories.UserFactory.build()
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity
