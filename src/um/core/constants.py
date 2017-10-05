"""Constants."""
from collections import namedtuple

from django.utils.translation import gettext_lazy as _


License = namedtuple('License', ['slug', 'title_short', 'title_long', 'url'])


cc_by = License(
    'cc-by',
    'CC BY 4.0',
    'Namensnennung 4.0 International (CC BY 4.0)',
    'https://creativecommons.org/licenses/by/4.0/deed.de',
    )

cc_by_sa = License(
    'cc-by-sa',
    'CC BY-SA 4.0',
    'Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International (CC BY-SA 4.0)',
    'https://creativecommons.org/licenses/by-sa/4.0/deed.de',
    )

LICENCE_CHOICES = (
    (cc_by.slug, cc_by.title_short),
    (cc_by_sa.slug, cc_by_sa.title_short),
)

LICENCE_CHOICES_LONG = (
    (cc_by.slug, cc_by.title_long),
    (cc_by_sa.slug, cc_by_sa.title_long),
)

LICENCE_NAMES_LONG = {
    cc_by.slug: cc_by.title_long,
    cc_by_sa.slug: cc_by_sa.title_long,
}

LICENCE_URLS = {
    cc_by.slug: cc_by.url,
    cc_by_sa.slug: cc_by_sa.url,
}

CHANGE_OPTIONS = (
    ('none', _('no changes')),
)
