from django.shortcuts import render, get_object_or_404, redirect
from .models import Workflow
from .forms import WorkflowForm


def workflow_list(request):
    workflows = Workflow.objects.all()
    return render(request, 'workflow_list.html', {'workflows': workflows})


def workflow_detail(request, pk):
    workflow = get_object_or_404(Workflow, pk=pk)
    return render(request, 'workflow_detail.html', {'workflow': workflow})


def workflow_create(request):
    if request.method == 'POST':
        form = WorkflowForm(request.POST)
        if form.is_valid():
            workflow = form.save()
            return redirect('workflow_detail', pk=workflow.pk)
    else:
        form = WorkflowForm()
    return render(request, 'workflow_form.html', {'form': form})


def workflow_edit(request, pk):
    workflow = get_object_or_404(Workflow, pk=pk)
    if request.method == 'POST':
        form = WorkflowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect('workflow_detail', pk=workflow.pk)
    else:
        form = WorkflowForm(instance=workflow)
    return render(request, 'workflow_form.html', {'form': form})


def workflow_delete(request, pk):
    workflow = get_object_or_404(Workflow, pk=pk)
    if request.method == 'POST':
        workflow.delete()
        return redirect('workflow_list')
    return render(request, 'workflow_confirm_delete.html', {'workflow': workflow})
