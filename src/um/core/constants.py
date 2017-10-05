"""Constants."""
from django.utils.translation import gettext_lazy as _


CC_BY = 'cc-by'
CC_BY_SHORT = 'CC BY 4.0'
CC_BY_LONG = 'Namensnennung 4.0 International (CC BY 4.0)'

CC_BY_SA = 'cc-by-sa'
CC_BY_SA_SHORT = 'CC BY-SA 4.0'
CC_BY_SA_LONG = 'Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International (CC BY-SA 4.0)'

LICENCE_CHOICES = (
    (CC_BY, CC_BY_SHORT),
    (CC_BY_SA, CC_BY_SA_SHORT),
)

LICENCE_CHOICES_LONG = (
    (CC_BY, CC_BY_LONG),
    (CC_BY_SA, CC_BY_SA_LONG),
)

LICENCE_NAMES_LONG = {
    CC_BY: CC_BY_LONG,
    CC_BY_SA: CC_BY_LONG,
}

LICENCE_URLS = {
    CC_BY: 'https://creativecommons.org/licenses/by/4.0/deed.de',
    CC_BY_SA: 'https://creativecommons.org/licenses/by-sa/4.0/deed.de',
}

CHANGE_OPTIONS = (
    ('none', _('no changes')),
)
