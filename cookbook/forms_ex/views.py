from collections import OrderedDict

import mistune
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import path
from django.utils.html import mark_safe
from django.views.generic import FormView, TemplateView, View

from . import forms


app_name = 'forms_ex'
urlpatterns = []

_INDEXED_VIEWS = []


def url(url_path, name=None, title=None):
    """Register view under the given url path."""
    if name is None:
        name = url_path.replace('/', '_')

    def decorator(view_class):
        urlpatterns.append(path(url_path, view_class.as_view(), name=name))
        if title is not None:
            view_name = f'{app_name}:{name}'
            _INDEXED_VIEWS.append((view_name, title))
        return view_class

    return decorator


class ConfirmAndRedirectToSelfMixin(SuccessMessageMixin):
    """View mixin to redirect form submission to the same page and confirm submission."""

    success_message = 'Form submission successful!'
    success_url = '/'  # Placeholder overriden by return value of `form_valid`.

    def form_valid(self, form):
        super().form_valid(form)
        return redirect(self.request.path_info)


@url('', name='index')
class IndexView(TemplateView):

    template_name = 'forms_ex/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        view_names_and_titles = _INDEXED_VIEWS
        # Update titles with markdown parser.
        view_names_and_titles = [(view_name, mark_safe(mistune.markdown(title)))
                                 for view_name, title in view_names_and_titles]
        context['view_names_and_titles'] = view_names_and_titles

        return context


@url('email_form', title='Basic form (`{{ form.as_p }}`)')
class EmailFormView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form.html'
    form_class = forms.EmailForm


@url('email_form_as_ul', title='Basic form (`{{ form.as_ul }}`)')
class EmailFormAsULView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_as_ul.html'
    form_class = forms.EmailForm


@url('email_form_as_table', title='Basic form (`{{ form.as_table }}`)')
class EmailFormAsTableView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_as_table.html'
    form_class = forms.EmailForm


@url('email_form_crispy_filter', title='Basic form (`{{ form|crispy }}`)')
class EmailFormCrispyFilterView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_crispy_filter.html'
    form_class = forms.EmailForm


@url('email_form_crispy_tag', title='Basic form (`{% crispy form %}`)')
class EmailFormCrispyTagView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_crispy_tag.html'
    form_class = forms.CrispyEmailForm


@url('email_modal', title='Modal form')
class EmailModalView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_modal.html'
    form_class = forms.EmailForm


@url('email_modal_with_ajax_submit', title='Modal form with ajax submission')
class EmailModalWithAjaxSubmitView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_modal_with_ajax_submit.html'
    form_class = forms.EmailForm


@url('email_modal_with_ajax_helper', title='Modal form with ajax crispy helper')
class EmailFormAjaxHelperView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_modal_with_ajax_helper.html'
    form_class = forms.CrispyAjaxEmailForm


@url('email_form_with_boolean', title='Basic form with boolean')
class EmailFormWithBooleanView(ConfirmAndRedirectToSelfMixin, FormView):

    template_name = 'forms_ex/email_form_crispy_filter.html'
    form_class = forms.EmailFormWithBoolean


@url('crispy_form_with_onclick', title='Crispy form with onclick handler')
class CrispyFormWithOnClickView(FormView):

    template_name = 'forms_ex/email_form_crispy_tag.html'
    form_class = forms.CrispyFormWithOnClick


@url('ajax_submit')
class AjaxSubmitView(View):

    def post(self, request, *args, **kwargs):
        return JsonResponse(request.POST)
