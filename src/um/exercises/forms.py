"""Form definitions."""
from braces.forms import UserKwargModelFormMixin

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Fieldset, Submit

from django import forms

from .models import Exercise


class ExerciseForm(UserKwargModelFormMixin, forms.ModelForm):
    """ModelForm for the Exercise model."""

    class Meta:  # noqa: D101
        model = Exercise
        fields = ['text', 'license']

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
                'exercise form',
                Field(
                    'text',
                    v_model='input',
                    css_class='editor-input',
                ),
            ),
        )
