from django import forms

SHIFT_CHOICES = (
    ("1", "morning"),
    ("2", "evening"),
    ("3", "night"),
)

ABSENCES_CHOICES = (
    ("1", "PTO")
)

class PTOForm(forms.Form):
    clock = forms.CharField()
    shift = forms.ChoiceField(choices=SHIFT_CHOICES)
    name = forms.CharField()
    first_day_absent = forms.DateField()
    last_day_absent = forms.DateField()
    hours = forms.IntegerField()
    absent_type = forms.ChoiceField(choices=ABSENCES_CHOICES)
    approving_supervisor = forms.CharField()
    email = forms.EmailField()


