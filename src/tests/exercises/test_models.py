"""Testing the models."""
from um.exercises import factories, models

import datetime

from mock import MagicMock

import pytest


# Some markdown text
MD = '''# Title
Dies ist ein [Markdown](https://daringfireball.net/projects/markdown/)-Dokument mit der Möglichkeit,
mathematische Ausdrücke einzugeben.

Die Vorschau folgt der CommonMark-Spezifikation. Alle mathematischen Ausdrücke nutzen die LaTeX-Syntax.

### Aufgabe 1
Hier ist eine Gleichung:

$$ 2 - x = 5 $$

### Aufgabe 2
Mathematische Ausdrücke wie $x=5$ können auch im Text stehen. Es geht aber auch komplizierter:

$$ \\int_\{0\}^{\infty} dx x^2 = 99 $$'''


class TestExerciseTimestampAttributes:

    def test_exercise_has_timestamps(self, db, mocker):
        mocker.patch('um.exercises.factories.Exercise.render_html')
        mocker.patch('um.exercises.factories.Exercise.render_tex')

        # GIVEN a saved exercise
        ex = factories.ExerciseFactory.create()

        # THEN it has time stamps
        assert ex.created.date() == datetime.date.today()
        assert ex.modified.date() == datetime.date.today()


class TestExerciseSaveMethod:

    def test_text_is_rendered_as_html_on_save(self, mocker):
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN a new Exercise with given Markdown/LaTeX text and empty text_html
        ex = factories.ExerciseFactory.build(text=MD)
        mocker.patch('um.exercises.models.Exercise.super_save', MagicMock(name="super_save"))

        # WHEN saving the exercise
        ex.save()

        # THEN there is the rendered HTML
        html = '''<h1>Title</h1>'''
        assert ex.text_html.startswith(html)

    def test_text_is_rendered_as_tex_on_save(self, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')

        # GIVEN a new Exercise with given Markdown/LaTeX text and empty text_tex
        ex = factories.ExerciseFactory.build(text=MD)
        mocker.patch('um.exercises.models.Exercise.super_save', MagicMock(name="super_save"))

        # WHEN saving the exercise
        ex.save()

        # THEN there is the rendered HTML
        tex = '''\section{Title}'''
        assert ex.text_tex.startswith(tex)


class TestExerciseRenderMethods:

    def test_render_html_renders_markdown_to_html(self):
        # GIVEN an exercise and a string of markdown text
        ex = factories.ExerciseFactory.build(text=MD)

        # WHEN calling the render_html method with this
        ex.render_html()

        # THEN the `text_html` model field is filled with HTML
        html = '''<h1>Title</h1>'''
        assert ex.text_html.startswith(html)

    def test_render_tex_renders_markdown_to_latex(self):
        # GIVEN an exercise and a string of markdown text
        ex = factories.ExerciseFactory.build(text=MD)

        # WHEN calling the render_html method with this
        ex.render_tex()

        # THEN the `text_tex` model field is filled with LaTeX
        tex = '''\section{Title}'''
        assert ex.text_tex.startswith(tex)
        assert '\[ 2 - x = 5 \]' in ex.text_tex


class TestExerciseDeleteMethod:
    """No real need to test this, as the functionality is inherited."""

    def no_test_delete_doesnt_remove_from_database(self, db, mocker):
        mocker.patch('um.exercises.factories.Exercise.render_html')
        mocker.patch('um.exercises.factories.Exercise.render_tex')

        # GIVEN an exercise
        ex = factories.ExerciseFactory.create()

        # WHEN deleting the exercise
        ex.delete()

        with pytest.raises(models.Exercise.DoesNotExist):
            models.Exercise.objects.get(id=ex.id)

        # THEN it is still there
        assert ex.is_removed

        # AND can be restored
        ex.is_removed = False
        ex.save()

        assert models.Exercise.objects.get(id=ex.id)


class TestExerciseExample:

    def test_exercise_example_has_string_representation(self):
        # GIVEN an exercise example
        example = factories.ExerciseExampleFactory.build()

        # THEN it has a reasonable string representation
        assert example.title in example.__str__()
