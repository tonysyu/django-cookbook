from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms


class EmailForm(forms.Form):

    email = forms.EmailField()


class CrispyEmailForm(forms.Form):

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(layout.Submit('submit', 'Save'))
