"""Exercise models."""
import os

# https://docs.python.org/3.6/library/shlex.html#shlex.quote
from shlex import quote

from django.db import models

from Naked.toolshed.shell import muterun_js
# >>> result = muterun_js('script.js', '"this is a string"')
# >>> result.stdout
# b'<p>this is a string</p>\n\n'
# >>>	
# scripth = './static/js/script.js'
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(MODULE_DIR, 'static/js/script.js')


class Exercise(models.Model):
    """The main exercise model."""

    text = models.TextField(verbose_name='Exercise text, Markdown/LaTeX')
    text_html = models.TextField(verbose_name='Exercise text, rendered as HTML')

    def render_html(self) -> None:
        """Render the raw Markdown/LaTeX `text` into HTML"""
        result = muterun_js(script, quote(self.text))
        self.text_html = result.stdout.decode()

    def super_save(self, *args, **kwargs) -> None:
        """Call the 'real' save() method."""
        super(Exercise, self).save(*args, **kwargs)

    def save(self, *args, **kwargs) -> None:
        """Do stuff when saving the Exercise."""
        self.render_html()

        self.super_save(*args, **kwargs)             # Call the "real" save() method.
