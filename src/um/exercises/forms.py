"""Form definitions."""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ExerciseForm'

        self.helper.add_input(Submit('submit', 'Submit'))
