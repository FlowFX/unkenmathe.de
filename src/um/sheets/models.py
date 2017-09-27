"""Sheets models."""

from django.db import models


class Sheet(models.Model):
    """The exercise sheet model."""

    # TimeStampedModel
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    exercises = models.ManyToManyField('exercises.Exercise')

    # TODO: add get_absolute_url()
