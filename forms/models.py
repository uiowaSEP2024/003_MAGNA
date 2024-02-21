from django.db import models
from django.utils.datetime_safe import datetime

from login.models import Employee


# Model for the AbsenceRequest form to keep track of all information
class AbsenceRequest(models.Model):
    # Assuming 'id' is the primary key, Django will create it automatically as an AutoField.

    clock_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    approval_status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ])
    shift_number = models.CharField(max_length=10, choices=[
        ("1st", "1st Shift"),
        ("2nd", "2nd Shift"),
        ("3rd", "3rd Shift"),
        ("4th", "4th Shift"),
    ])
    hours_gone = models.IntegerField()
    absence_type = models.CharField(max_length=50)
    approval = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="approved_forms",
        db_column='approval_id',
        null=True,  # Allow null values
        blank=True  # Allow the field to be blank in forms and admin
    )

    filled_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="filled_forms",
        db_column='filled_by_id',
        null=True,  # Allow null values
        blank=True  # Allow the field to be blank in forms and admin
    )

    class Meta:
        # Set the table name
        db_table = 'forms_absence_request'


# Model to keep track of allowed absent days on the Calendar
class AbsentDaysAllowed(models.Model):
    shiftDay = models.DateField(unique=True)  # Ensures each date is only entered once
    allowedAbsent = models.IntegerField(default=0)

    def __str__(self):
        # Return a string representing the shift schedule
        return f"{self.shiftDay}: {self.allowedAbsent} allowed absents"

    class Meta:
        # Set the table name
        db_table = 'absent_days_allowed'







