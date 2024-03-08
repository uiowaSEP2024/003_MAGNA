from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.forms import modelform_factory
from django.shortcuts import render, redirect


class Workflow(models.Model):
    """Model representing a workflow."""

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("manager_review", "Manager Review"),
        ("HR_review", "HR Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="submitted"
    )

    def edit_workflow_ids(request, pk):
        absence_request = get_object_or_404(AbsenceRequest, pk=pk)
        WorkflowIdForm = modelform_factory(AbsenceRequest, fields=['workflow_ids'])

        if request.method == 'POST':
            form = WorkflowIdForm(request.POST, instance=absence_request)
            if form.is_valid():
                form.save()
                return redirect('list_absence_requests')  # Redirect to the listing view
        else:
            form = WorkflowIdForm(instance=absence_request)

        return render(request, 'edit_workflow_ids.html', {'form': form, 'absence_request': absence_request})

    def absence_request_view(request):
        if request.method == 'POST':
            form = AbsenceRequestForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('some-view-name')  # Redirect to a new URL
        else:
            form = AbsenceRequestForm()  # An unbound form

        return render(request, 'your_template_name.html', {'form': form})