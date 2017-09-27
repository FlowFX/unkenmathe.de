"""Unit tests for the forms."""
from um.core import factories
from um.exercises import forms

import pytest

from authtools.models import User


class TestExerciseForms:

    TESTPARAMS_EXERCISE = [
        ('$5x + 4 = 20$.', 'cc-by', False, '', True),  # source is not required
        ('$5x + 4 = 20$.', 'cc-by-sa', False, '', True),
        ('$5x + 4 = 20$.', 'cc-by', True, 'https://de.serlo.org/mathe/xxx', True),  # include a source
        ('', 'cc-by', False, '', False),  # text is required
        ('$5x + 4 = 20$.', '', False, '', False),  # license is required
        ('$5x + 4 = 20$.', 'cc-by-XX', False, '', False),  # license is one of cc-by|cc-by-sa
        ('$5x + 4 = 20$.', 'cc-by', True,  '', False),  # if source exists, source URL is required
    ]

    @pytest.mark.parametrize('text, license, source, source_url, validity', TESTPARAMS_EXERCISE)
    def test_exercise_form(self, db, text, license, source, source_url, validity):
        """Unit test the Exercise Form."""
        # GIVEN a user and form data
        users = factories.UserFactory.create_batch(2)

        data={
            # 'author': User.objects.get(pk=author.id),
            'text': text,
            'license': license,
        }
        if source:
            data['source'] = User.objects.get(pk=users[0].id).id
            data['source_url'] = source_url

        # WHEN submitting the form as the original author
        form = forms.ExerciseForm(
            data=data,
            user=users[1]
        )

        # THEN it validates -- or not
        assert form.is_valid() is validity
