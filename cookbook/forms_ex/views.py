from collections import OrderedDict

import mistune
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.html import mark_safe
from django.views.generic import FormView, TemplateView, View

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

        view_names_and_titles = OrderedDict([
            ('forms_ex:email_form', 'Basic form (`{{ form.as_p }}`)'),
            ('forms_ex:email_form_as_ul', 'Basic form (`{{ form.as_ul }}`)'),
            ('forms_ex:email_form_as_table', 'Basic form (`{{ form.as_table }}`)'),
            ('forms_ex:email_form_crispy_filter', 'Basic form (`{{ form|crispy }}`)'),
            ('forms_ex:email_form_crispy_tag', 'Basic form (`{% crispy form %}`)'),
            ('forms_ex:email_modal', 'Modal form'),
            ('forms_ex:email_modal_with_ajax_submit', 'Modal form with ajax submission'),
            ('forms_ex:email_form_with_boolean', 'Basic form with boolean'),
            ('forms_ex:crispy_form_with_onclick', 'Crispy form with onclick handler'),
        ])
        # Update titles with markdown parser.
        for view_name, title in view_names_and_titles.items():
            view_names_and_titles[view_name] = mark_safe(mistune.markdown(title))
        context['view_names_and_titles'] = view_names_and_titles

        return context


class EmailFormView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form.html'
    form_class = forms.EmailForm


class EmailFormCrispyTagView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_crispy_tag.html'
    form_class = forms.CrispyEmailForm


class EmailFormWithBooleanView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_crispy_filter.html'
    form_class = forms.EmailFormWithBoolean


class CrispyFormWithOnClickView(FormView):

    template_name = 'forms_ex/email_form_crispy_tag.html'
    form_class = forms.CrispyFormWithOnClick


class AjaxSubmitView(View):

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return JsonResponse(request.POST)
