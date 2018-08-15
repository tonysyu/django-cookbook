from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms


class EmailForm(forms.Form):

    email = forms.EmailField()


class CrispyEmailForm(forms.Form):
    """Form rendered using `{% crispy form %}` tag.

    Using crispy tag allows the form layout (e.g. a Save button) to be delegated to the form.
    """

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(layout.Submit('submit', 'Save'))


class EmailFormWithBoolean(forms.Form):
    """Form with boolean field must set `required=False` to allow boolean to be unchecked.

    See discussion at https://stackoverflow.com/questions/8542839
    """

    email = forms.EmailField()
    spam_me = forms.BooleanField(required=False)


class CrispyFormWithOnClick(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # Rather than adding a submit button, add a 
        self.helper.add_input(
            layout.Button(
                name='fire',
                value='Fire',
                onclick="alert('Fired!')",
                css_class='btn btn-primary',
            ),
        )
