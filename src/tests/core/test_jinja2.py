"""Unit-test the Jinja2 environment for LaTeX templates."""
from jinja2 import Environment

from um.core.jinja2 import jinja2_latex_env
from um.exercises import factories


class TestJinja2Environment:

    def test_environment(self):
        env = jinja2_latex_env
        assert isinstance(env, Environment)

    def test_env_renders_correct_latex(self):
        # GIVEN a basic template
        env = jinja2_latex_env
        template = env.get_template('exercise_detail.j2.tex')

        # AND an exercise
        ex = factories.ExerciseFactory.build()

        context = {'exercise': ex, }

        # WHEN rendering the template
        latex: str = template.render(context)

        # THEN it's correct LaTeX code
        assert latex.startswith('\\documentclass{article}')
        assert latex.endswith('\\end{document}')
