"""Core models."""
from django.db import models


class TimeStampedMixin(object):
    """An model mixin that provides self-updating ``created`` and ``modified`` fields."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
