"""Form definitions."""
from braces.forms import UserKwargModelFormMixin

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Submit

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Sheet


class SheetForm(UserKwargModelFormMixin, forms.ModelForm):
    """ModelForm for the Sheet model."""

    class Meta:  # noqa: D101
        model = Sheet
        fields = ['exercises']

    def __init__(self, *args, **kwargs):
        """Add crispy-forms helper and layout to form."""
        super(SheetForm, self).__init__(*args, **kwargs)

        # add Crispy Forms foo
        self.helper = FormHelper()
        self.helper.form_id = 'id-SheetForm'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.layout = Layout(
            Fieldset(
                _('sheet form'),
                'exercises',
            ),
        )
