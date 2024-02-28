from django.forms import ModelForm
from .models import Workflow


class WorkflowForm(ModelForm):
    class Meta:
        model = Workflow
        fields = ['name', 'description']
