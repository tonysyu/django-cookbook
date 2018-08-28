from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.utils import TEMPLATE_PACK
from django import forms
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.utils.html import mark_safe


class EmailForm(forms.Form):

    email = forms.EmailField()


class CrispyEmailForm(forms.Form):
    """Form rendered using `{% crispy form %}` tag.

    Using crispy tag allows the form layout (e.g. a Save button) to be delegated to the form.
    """

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(layout.Submit('submit', 'Save'))


class CrispyAjaxEmailForm(forms.Form):
    """Form rendered using `{% crispy form %}` tag and embedded javascript."""

    email = forms.EmailField()
    media_template = 'forms_ex/snippets/ajax_submission.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse('forms_ex:ajax_submit')
        self.helper.add_input(layout.Submit('submit', 'Save'))

    @property
    def media(self):
        return mark_safe(render_to_string(self.media_template, {'helper': self.helper}))


class CrispyAjaxModalEmailForm(CrispyAjaxEmailForm):
    """Modal form rendered using `{% crispy form %}` tag and embedded javascript for modal."""

    media_template = 'forms_ex/snippets/modal_ajax_submission.html'


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
