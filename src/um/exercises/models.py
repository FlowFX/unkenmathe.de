"""Exercise models."""
from django.db import models


class Exercise(models.Model):
    """The main exercise model."""

    text = models.TextField(verbose_name='Exercise text, Markdown/LaTeX')
    text_html = models.TextField(verbose_name='Exercise text, rendered as HTML')

    def render_html(self) -> None:
        """Render the raw Markdown/LaTeX `text` into HTML"""
        self.text_html = self.text
        self.text_html = '<h1>Title</h1>'

    def super_save(self, *args, **kwargs) -> None:
        """Call the 'real' save() method."""
        super(Exercise, self).save(*args, **kwargs)

    def save(self, *args, **kwargs) -> None:
        """Do stuff when saving the Exercise."""
        self.text_html = '<h2>Header</h2>'

        self.super_save(*args, **kwargs)             # Call the "real" save() method.
