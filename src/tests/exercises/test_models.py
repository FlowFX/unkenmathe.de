"""Testing the models."""
from um.exercises import factories

from mock import MagicMock


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


class TestExerciseModel:

    def test_text_is_rendered_as_html_on_save(self, mocker):
        # GIVEN a new Exercise with given Markdown/LaTeX text and empty text_html
        ex = factories.ExerciseFactory.build(text=MD)
        mocker.patch('um.exercises.models.Exercise.super_save', MagicMock(name="super_save"))

        # WHEN saving the exercise
        ex.save()

        # THEN there is the rendered HTML
        html = '''<h1>Title</h1>'''
        assert ex.text_html.startswith(html)

    def test_text_is_rendered_as_tex_on_save(self, mocker):
        # GIVEN a new Exercise with given Markdown/LaTeX text and empty text_tex
        ex = factories.ExerciseFactory.build(text=MD)
        mocker.patch('um.exercises.models.Exercise.super_save', MagicMock(name="super_save"))

        # WHEN saving the exercise
        ex.save()

        # THEN there is the rendered HTML
        tex = '''\section{Title}'''
        assert ex.text_tex.startswith(tex)

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
