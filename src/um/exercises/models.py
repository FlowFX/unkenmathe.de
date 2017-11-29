"""Exercise models."""
import os
import subprocess
import uuid

from django.conf import settings
from django.shortcuts import reverse

from model_utils.models import SoftDeletableModel

from um.core.constants import CHANGE_OPTIONS, LICENCE_CHOICES, LICENCE_NAMES_LONG, LICENCE_URLS

# https://docs.python.org/3.6/library/shlex.html#shlex.quote
from shlex import quote

from django.db import models

import pypandoc

# get path to node script
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(MODULE_DIR, 'static/js/script.js')

# get path to node binary
node = os.path.expanduser('~/.nvm/versions/node/v6.11.2/bin/node')
if not os.path.exists(node):  # pragma: no cover
    # if nvm is not used, use system binary (i.e. on Travis CI)
    node = 'node'


class Exercise(SoftDeletableModel):
    """The main exercise model."""

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    slug = models.SlugField(max_length=5)

    # TimeStampedModel
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    license = models.CharField(
        max_length=15,
        choices=LICENCE_CHOICES,
        default='cc-by'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author',
        on_delete=models.PROTECT,
    )
    is_original = models.BooleanField(default=True)
    original_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
    )
    source_url = models.URLField(blank=True)
    changes = models.CharField(
        max_length=15,
        choices=CHANGE_OPTIONS,
        default='none',
    )

    text = models.TextField(verbose_name='Exercise text, Markdown/LaTeX')
    text_html = models.TextField(verbose_name='Exercise text, rendered as HTML')
    text_tex = models.TextField(verbose_name='Exercise text, rendered as LaTeX')

    def __str__(self):
        """Format str(obj) response."""
        return '#{}'.format(self.slug)

    @property
    def license_url(self) -> str:
        """Return the URL to the chosen license."""
        return LICENCE_URLS[self.license]

    @property
    def license_name_long(self) -> str:
        """Return the long form title of the chosen license."""
        return LICENCE_NAMES_LONG[self.license]

    @property
    def url(self) -> str:
        """Return canonical URL for this exercise."""
        return self.get_absolute_url()

    def get_absolute_url(self) -> str:
        """Return URL of the exercise's DetailView."""
        return reverse('exercises:detail', kwargs={'slug': self.slug})

    def render_html(self) -> None:
        """Render the raw Markdown/LaTeX `text` into HTML."""
        string = quote(self.text)
        command = f'{node} {script} {string}'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

        self.text_html = result.decode()

    def render_tex(self) -> None:
        """Render the raw Markdown/LaTeX `text` into LaTeX code."""
        result = pypandoc.convert_text(self.text, 'latex', 'markdown')
        self.text_tex = result

    def super_save(self, *args, **kwargs) -> None:
        """Call the 'real' save() method."""
        super(Exercise, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = str(self.id + 10000)
            self.save()

    def save(self, *args, **kwargs) -> None:
        """Do stuff when saving the Exercise."""
        self.render_html()
        self.render_tex()

        self.super_save(*args, **kwargs)             # Call the "real" save() method.


class ExerciseExample(models.Model):
    """An exercise example with title and description.

    For the Howto page.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        """Format str(obj) response."""
        return 'Beispiel {}: {}'.format(self.id, self.title)
