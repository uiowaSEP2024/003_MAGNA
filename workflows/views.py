from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from forms.models import AbsenceRequest

from .models import Workflow


@user_passes_test(lambda u: u.is_superuser)
def view_workflows(request):
    """View all workflows."""
    workflows = Workflow.objects.all()
    return render(request, "workflows/list.html", {"workflows": workflows})


@user_passes_test(lambda u: u.is_superuser)
def edit_workflow(request, pk):
    """Edit a workflow."""
    workflow = get_object_or_404(Workflow, pk=pk)
    if request.method == "POST":
        # Form submission logic here
        # Update workflow object and save
        workflow.save()
        return redirect("workflows:list")
    return render(request, "workflows/edit.html", {"workflow": workflow})


@user_passes_test(lambda u: u.is_superuser)
def delete_workflow(request, pk):
    """Delete a workflow."""
    workflow = get_object_or_404(Workflow, pk=pk)
    if request.method == "POST":
        workflow.delete()
        return redirect("workflows:list")
    return render(request, "workflows/confirm_delete.html", {"workflow": workflow})


def manager_review(request, pk):
    """Manager review of an absence request."""
    absence_request = get_object_or_404(
        AbsenceRequest, pk=pk, workflow__status="submitted"
    )
    if request.method == "POST":
        # Form submission logic here
        # Update absence request object and workflow status
        absence_request.workflow.status = "manager_review"
        absence_request.save()
        return redirect("workflows:list")
    return render(
        request, "workflows/review.html", {"absence_request": absence_request}
    )


def HR_review(request, pk):
    """HR review of an absence request."""
    absence_request = get_object_or_404(
        AbsenceRequest, pk=pk, workflow__status="manager_review"
    )
    if request.method == "POST":
        # Form submission logic here
        # Update absence request object and workflow status
        absence_request.workflow.status = "HR_review"
        absence_request.save()
        return redirect("workflows:list")
    return render(
        request, "workflows/review.html", {"absence_request": absence_request}
    )
