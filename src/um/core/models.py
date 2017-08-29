"""Core models."""
from django.db import models

from model_utils.managers import SoftDeletableManager


class TimeStampedModel(models.Model):
    """An abstract base class model that provides self-updating ``created`` and ``modified`` fields."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:  # noqa: D101
        abstract = True


class SoftDeletableMixin(object):
    """An model mixin with a ``is_removed`` field that marks entries that are not going to be used anymore, but are kept in db for any reason.

    Default manager returns only not-removed entries.

    This is copied directly from django-model-utils: https://github.com/jazzband/django-model-utils/blob/master/model_utils/models.py
    """
    is_removed = models.BooleanField(default=False)

    objects = SoftDeletableManager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        Soft delete object (set its ``is_removed`` field to True).
        Actually delete object if setting ``soft`` to False.
        """
        if soft:
            self.is_removed = True
            self.save(using=using)
        else:
            return super(SoftDeletableMixin, self).delete(using=using, *args, **kwargs)
