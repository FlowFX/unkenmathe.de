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
            'author',
            'original_author',
            'source_url',
            ]

        labels = {
            'text': None,
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
                _('exercise text'),
                Field(
                    'text',
                    v_model='input',
                    css_class='editor-input',
                ),
                'license',
                'author',
                'original_author',
                'source_url',
            ),
        )
        self.fields['text'].label = False
        self.fields['author'].required = False
        self.fields['original_author'].required = False
        self.fields['source_url'].required = False

        if self.user and not self.user.is_staff:
            # don't let normal users change the author field
            self.fields['author'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(ExerciseForm, self).clean()
        original_author = cleaned_data.get('original_author')
        source_url = cleaned_data.get('source_url')

        if original_author and source_url == '':
            # If source is given, then a source URL is required.
            raise forms.ValidationError(
                _('Please provide a URL for the source.')
            )
