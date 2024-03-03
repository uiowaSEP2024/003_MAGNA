from django import forms


class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = JobPDFs
        fields = ['title', 'pdf_file']