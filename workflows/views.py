from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from forms.models import AbsenceRequest
from django.shortcuts import render, redirect
from .models import FormEmailSetting, Workflow
from .forms import FormEmailSettingForm


def workflows(request):
    """
    Renders the workflow page.

    Args:
    - request: the HTTP request object

    Returns:
    - Rendered workflows.html template
    """
    form_type = 'time_off'
    return manage_email_recipients(request)


def manage_email_recipients(request):
    form_types = ['time_off', 'job_postings', 'work_orders']
    form_email_settings = {}

    for form_type in form_types:
        form_email_setting = FormEmailSetting.objects.filter(form_type=form_type).first()
        if not form_email_setting:
            form_email_setting = FormEmailSetting(form_type=form_type)

        if request.method == 'POST' and request.POST.get(f'form_type_{form_type}'):
            email_recipients = request.POST.get(f'email_recipients_{form_type}', '')
            form_email_setting.email_recipients = email_recipients
            form_email_setting.save()

        form_email_settings[form_type] = form_email_setting

    return render(request, 'workflows.html', {'form_email_settings': form_email_settings, 'form_types': form_types})