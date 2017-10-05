"""Constants."""
from django.utils.translation import gettext_lazy as _


CC_BY = 'cc-by'
CC_BY_SA = 'cc-by-sa'

LICENCE_CHOICES = (
    (CC_BY, 'CC BY 4.0'),
    (CC_BY_SA, 'CC BY-SA 4.0'),
)

LICENCE_CHOICES_LONG = (
    (CC_BY, 'Namensnennung 4.0 International (CC BY 4.0)'),
    (CC_BY_SA, 'Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International (CC BY-SA 4.0)'),
)

LICENCE_URLS = {
    CC_BY: 'https://creativecommons.org/licenses/by/4.0/deed.de',
    CC_BY_SA: 'https://creativecommons.org/licenses/by-sa/4.0/deed.de',
}

CHANGE_OPTIONS = (
    ('none', _('no changes')),
)
