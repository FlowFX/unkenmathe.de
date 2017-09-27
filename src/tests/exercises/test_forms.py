"""Unit tests for the forms."""
from um.core import factories
from um.exercises import forms

import pytest


class TestExerciseForms:

    TESTPARAMS_EXERCISE = [
        ('$5x + 4 = 20$.', 'cc-by',    True,  'https://de.serlo.org/mathe/xxx', True),
        ('$5x + 4 = 20$.', 'cc-by',    False, '', True),  # source is not required
        ('$5x + 4 = 20$.', 'cc-by-sa', False, '', True),
        ('$5x + 4 = 20$.', 'cc-by-nd', False, '', True),
        ('',               'cc-by',    False, '', False),  # text is required
        ('$5x + 4 = 20$.', '',         False, '', False),  # license is required
        ('$5x + 4 = 20$.', 'cc-by-XX', False, '', False),  # license is one of cc-by|cc-by-sa|cc-by-na
        # TODO: Test this case
        # ('$5x + 4 = 20$.', 'cc-by',    True,  '', False),  # if source exists, source URL is required
    ]

    @pytest.mark.parametrize('text, license, source, source_url, validity', TESTPARAMS_EXERCISE)
    def test_exercise_form(self, text, license, source, source_url, validity):
        """Unit test the Exercise Form."""
        # GIVEN form data
        data={
            'text': text,
            'license': license,
            # 'source': source,
            # 'source_url': source_url,
        }

        # WHEN submitting the form
        form = forms.ExerciseForm(
            data=data,
            user=factories.UserFactory.build()
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity
