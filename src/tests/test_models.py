"""Testing the models."""
from um.exercises import factories

from mock import MagicMock


class TestExerciseModel:

    def test_text_is_rendered_as_html_on_save(self, mocker):
        # GIVEN a new Exercise with given Markdown/LaTeX text and empty text_html
        ex = factories.ExerciseFactory.build(
            text='## Header',
        )
        assert ex.text_html == ''

        mocker.patch('um.exercises.models.Exercise.super_save', MagicMock(name="super_save"))

        # WHEN saving the exercise
        ex.save()

        # THEN there is the rendered HTML
        html = '''<h2>Header</h2>'''
        assert ex.text_html.startswith(html)
