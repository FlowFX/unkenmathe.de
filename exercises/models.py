"""Exercise models."""
from django.db import models


class Exercise(models.Model):
    """The main exercise model."""

    text = models.TextField(verbose_name='Exercise text')
