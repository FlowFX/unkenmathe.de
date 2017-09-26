"""Sheets models."""

from django.db import models

from um.exercises.models import Exercise



class Sheet(models.Model):
    """The exercise sheet model."""

    # TimeStampedModel
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    exercises = models.ManyToManyField('exercises.Exercise')
