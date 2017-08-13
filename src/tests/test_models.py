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

    def test_render_html_renders_markdown(self):
        # GIVEN an exercise and a string of markdown text
        md = '''# Title
                  This is some **bold** text.
                  '''
        ex = factories.ExerciseFactory.build(
            text=md,
        )
        # WHEN calling the render_html method with this
        ex.render_html()

        # THEN the `text_html` model field is filled with HTML
        html = '''<h1>Title</h1>'''
        assert ex.text_html.startswith(html)
