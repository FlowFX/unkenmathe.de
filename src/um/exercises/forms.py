"""Form definitions."""
from braces.forms import UserKwargModelFormMixin

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Field, Fieldset, HTML, Submit

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Exercise


class ExerciseForm(UserKwargModelFormMixin, forms.ModelForm):
    """ModelForm for the Exercise model."""

    class Meta:  # noqa: D101
        model = Exercise
        fields = [
            'text',
            'license',
            'source',
            'source_url',
            ]

        labels = {
            'text': 'Aufgabentext',
        }
        help_texts = {
            'text': 'Markdown und LaTeX mit $ und $$.',
        }

    def __init__(self, *args, **kwargs):
        """Add crispy-forms helper and layout to form."""
        super(ExerciseForm, self).__init__(*args, **kwargs)

        # add Crispy Forms foo
        self.helper = FormHelper()
        self.helper.form_id = 'id-ExerciseForm'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.layout = Layout(
            Fieldset(
                _('exercise form'),
                Field(
                    'text',
                    v_model='input',
                    css_class='editor-input',
                ),
                'license',
                'source',
                'source_url',
            ),
        )
        self.fields['source'].required = False
        self.fields['source_url'].required = False

    def clean(self):
        cleaned_data = super(ExerciseForm, self).clean()
        source = cleaned_data.get('source')
        source_url = cleaned_data.get('source_url')

        print(source)

        if source and source_url == '':
            # If source is given, then a source URL is required.
            raise forms.ValidationError(
                _('Please provide a URL for the source.')
            )
