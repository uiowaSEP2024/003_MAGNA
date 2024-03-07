from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from forms.models import AbsenceRequest
from .models import Workflow


@login_required
def edit_workflow(request, form_id):
    # View for editing a form's workflow
    form = YourFormModel.objects.get(id=form_id)
    if request.method == "POST":
        # Update form.workflow_ids based on POST data
        form.workflow_ids = request.POST.getlist('workflow_ids')  # Adjust as needed
        form.save()
        return redirect('workflow_list')
    return render(request, 'workflow_form.html', {'form': form})

@login_required
def view_received_forms(request):
    # View for forms a user receives based on their ID
    user_id = request.user.id  # Adjust based on your user model
    received_forms = YourFormModel.objects.filter(workflow_ids__contains=[user_id])
    return render(request, 'received_forms.html', {'forms': received_forms})

@login_required
def view_workflows(request):
    # View for listing all workflows
    forms = YourFormModel.objects.all()
    return render(request, 'workflow_list.html', {'forms': forms})


@login_required
def delete_workflow(request, pk):
    """Delete a workflow."""
    workflow = get_object_or_404(Workflow, pk=pk)
    if request.method == "POST":
        workflow.delete()
        return redirect("workflows:list")
    return render(request, "workflows/confirm_delete.html", {"workflow": workflow})