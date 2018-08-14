from collections import OrderedDict

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import FormView, TemplateView

from . import forms


class ConfirmAndRedirectToSelfMixin(SuccessMessageMixin):
    """View mixin to redirect form submission to the same page and confirm submission."""

    success_message = 'Form submission successful!'
    success_url = '/'  # Placeholder overriden by return value of `form_valid`.

    def form_valid(self, form):
        super().form_valid(form)
        return redirect(self.request.path_info)


class IndexView(TemplateView):

    template_name = 'forms_ex/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_names_and_titles'] = OrderedDict([
            ('forms_ex:email_form', 'Basic form'),
            ('forms_ex:email_form_as_ul', 'Basic form using `as_ul`'),
            ('forms_ex:email_form_as_table', 'Basic form using `as_table`'),
            ('forms_ex:email_form_crispy_filter', 'Basic form using crispy filter'),
            ('forms_ex:email_modal', 'Modal form'),
        ])
        return context


class EmailFormView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form.html'
    form_class = forms.EmailForm


class EmailModalView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_modal.html'
    form_class = forms.EmailForm
