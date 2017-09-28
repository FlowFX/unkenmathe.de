"""Constants."""
from django.utils.translation import gettext_lazy as _


CC_BY = 'cc-by'
CC_BY_SA = 'cc-by-sa'
# CC_BY_ND = 'cc-by-nd'

LICENCE_CHOICES = (
    (CC_BY, 'CC BY'),
    (CC_BY_SA, 'CC BY-SA'),
    # (CC_BY_ND, 'CC BY-ND'),
)

LICENCE_URLS = {
    CC_BY: 'https://creativecommons.org/licenses/by/4.0/',
    CC_BY_SA: 'https://creativecommons.org/licenses/by-sa/4.0/',
    # CC_BY_ND: 'https://creativecommons.org/licenses/by-nd/4.0/'
}

CHANGE_OPTIONS = (
    ('none', _('no changes')),
)
