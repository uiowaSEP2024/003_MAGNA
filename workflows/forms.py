from django import forms
from .models import FormEmailSetting

class FormEmailSettingForm(forms.ModelForm):
    class Meta:
        model = FormEmailSetting
        fields = ['email_recipients']