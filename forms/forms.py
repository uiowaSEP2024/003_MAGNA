from django import forms
from .models import JobPDFs


class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = JobPDFs
        fields = ['title', 'pdf_file']