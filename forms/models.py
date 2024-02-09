from django.db import models

from login.models import Employee


class AbsenceRequest(models.Model):
    """Model for Absence Requests"""

    APPROVAL_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    SHIFT_CHOICES = [
        ("1st", "1st Shift"),
        ("2nd", "2nd Shift"),
        ("3rd", "3rd Shift"),
        ("4th", "4th Shift"),
    ]

    start_date = models.DateField()
    end_date = models.DateField()
    approval_status = models.CharField(max_length=20, choices=APPROVAL_CHOICES)
    shift_number = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    hours_gone = models.IntegerField()
    absence_type = models.CharField(max_length=50)
    approval = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="approved_forms"
    )
    filled_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="filled_forms"
    )
