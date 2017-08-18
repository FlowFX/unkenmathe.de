"""Exercise models."""
import os
import subprocess

# https://docs.python.org/3.6/library/shlex.html#shlex.quote
from shlex import quote

from django.db import models

import pypandoc

# get path to node script
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(MODULE_DIR, 'static/js/script.js')

# get path to node binary
node = os.path.expanduser('~/.nvm/versions/node/v6.11.2/bin/node')
if not os.path.exists(node):
    # if nvm is not used, use system binary (i.e. on Travis CI)
    node = 'node'


class Exercise(models.Model):
    """The main exercise model."""

    text = models.TextField(verbose_name='Exercise text, Markdown/LaTeX')
    text_html = models.TextField(verbose_name='Exercise text, rendered as HTML')
    text_tex = models.TextField(verbose_name='Exercise text, rendered as LaTeX')

    def render_html(self) -> None:
        """Render the raw Markdown/LaTeX `text` into HTML."""
        string = quote(self.text)
        command = f'{node} {script} {string}'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

        self.text_html = result.decode()

    def render_tex(self) -> None:
        """Render the raw Markdown/LaTeX `text` into LaTeX code."""
        result = pypandoc.convert_text(self.text, 'tex', 'md')
        self.text_tex = result

    def super_save(self, *args, **kwargs) -> None:
        """Call the 'real' save() method."""
        super(Exercise, self).save(*args, **kwargs)

    def save(self, *args, **kwargs) -> None:
        """Do stuff when saving the Exercise."""
        self.render_html()
        self.render_tex()

        self.super_save(*args, **kwargs)             # Call the "real" save() method.
