from django.urls import path

from . import views


app_name = 'forms_ex'
urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='index',
    ),
    path(
        'email_form',
        views.EmailFormView.as_view(),
        name='email_form',
    ),
    path(
        'email_form_as_ul',
        views.EmailFormView.as_view(template_name='forms_ex/email_form_as_ul.html'),
        name='email_form_as_ul',
    ),
    path(
        'email_form_as_table',
        views.EmailFormView.as_view(template_name='forms_ex/email_form_as_table.html'),
        name='email_form_as_table',
    ),
    path(
        'email_form_crispy_filter',
        views.EmailFormView.as_view(template_name='forms_ex/email_form_crispy_filter.html'),
        name='email_form_crispy_filter',
    ),
    path(
        'email_form_crispy_tag',
        views.EmailFormCrispyTagView.as_view(),
        name='email_form_crispy_tag',
    ),
    path(
        'email_modal',
        views.EmailModalView.as_view(),
        name='email_modal',
    ),
    path(
        'email_form_with_boolean',
        views.EmailFormWithBooleanView.as_view(),
        name='email_form_with_boolean',
    ),
    path(
        'crispy_form_with_onclick',
        views.CrispyFormWithOnClickView.as_view(),
        name='crispy_form_with_onclick',
    ),
]
