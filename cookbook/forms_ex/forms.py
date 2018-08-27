from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.utils import TEMPLATE_PACK
from django import forms
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.utils.html import mark_safe


JAVASCRIPT_TEMPLATE_WRAPPER = """
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"
            integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
            crossorigin="anonymous">
    </script>
    <script charset="utf-8">
        {}
    </script>
"""

class AjaxFormHelper(FormHelper):

    def render_layout(self, form, context, template_pack=TEMPLATE_PACK):
        html = super().render_layout(form, context, template_pack=template_pack)
        js = render_to_string('forms_ex/snippets/modal_ajax_submission.js', {'helper': self})
        js = JAVASCRIPT_TEMPLATE_WRAPPER.format(js)
        return mark_safe(html + js)


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
    """Form rendered using `{% crispy form %}` tag and `AjaxFormHelper`."""

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = AjaxFormHelper(self)
        self.helper.form_action = reverse('forms_ex:ajax_submit')
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
