from django import forms
from .models import JobPDFs


class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = JobPDFs
        fields = ['title', 'pdf_file']

class PDFContentForm(forms.Form):
    title = forms.CharField(max_length=200, label='PDF Title')
    content = forms.CharField(widget=forms.Textarea, label='PDF Content')