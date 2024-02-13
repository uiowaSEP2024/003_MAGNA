from django.db import models

from login.models import Employee


class AbsenceRequest(models.Model):
    """FILL IN"""

    start_date = models.DateField()
    end_date = models.DateField()
    approval_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
    )
    shift_number = models.CharField(
        max_length=10,
        choices=[
            ("1st", "1st Shift"),
            ("2nd", "2nd Shift"),
            ("3rd", "3rd Shift"),
            ("4th", "4th Shift"),
        ],
    )
    hours_gone = models.IntegerField()
    absence_type = models.CharField(max_length=50)
    approval = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="approved_forms",
        db_column="approval_id",
        null=True,  # Allow null values
        blank=True,  # Allow the field to be blank in forms and admin
    )

    filled_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="filled_forms",
        db_column="filled_by_id",
        null=True,  # Allow null values
        blank=True,  # Allow the field to be blank in forms and admin
    )

    class Meta:
        db_table = "forms_absencerequest"
