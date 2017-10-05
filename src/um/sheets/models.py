"""Sheets models."""
from django.conf import settings
from django.db import models
from django.shortcuts import reverse


class Sheet(models.Model):
    """The exercise sheet model."""

    # TimeStampedModel
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sheets',
        null=True,
        on_delete=models.SET_NULL,
    )

    exercises = models.ManyToManyField('exercises.Exercise')

    @property
    def url(self) -> str:
        """Return canonical URL for this exercise sheet."""
        return self.get_absolute_url()

    def get_absolute_url(self) -> str:
        """Return URL of the sheet's DetailView."""
        return reverse('sheets:detail', kwargs={'pk': self.pk})
