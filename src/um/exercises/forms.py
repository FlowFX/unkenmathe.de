"""Form definitions."""
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Field, Fieldset, Submit

from django import forms

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['text']

        labels = {
            'text': 'Aufgabentext',
        }
        help_texts = {
            'text': 'Markdown und LaTeX mit $ und $$.',
        }

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
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
                Div(
                    id='preview',
                    v_html='compiledMarkdown',
                    css_class='editor-preview',
                ),
            ),
        )
