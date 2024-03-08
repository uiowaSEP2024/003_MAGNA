from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from forms.models import AbsenceRequest
from .models import Workflow


def edit_workflow(request):
    """
    Renders the editing workflow page.

    Args:
    - request: the HTTP request object

    Returns:
    - Rendered workflow_edit.html template
    """
    return render(request, "workflow_edit.html")