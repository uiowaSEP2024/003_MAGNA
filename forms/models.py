from django.db import models
from django.utils.datetime_safe import datetime

from login.models import Employee


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
        db_table = 'forms_absence_request'


class AbsentDaysAllowed(models.Model):
    shiftDay = models.DateField(unique=True)  # Ensures each date is only entered once
    allowedAbsent = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.shiftDay}: {self.allowedAbsent} allowed absents"

    class Meta:
        db_table = 'absent_days_allowed'

class requestedDays(models.Model):
    absence_request = models.ForeignKey(AbsenceRequest, on_delete=models.CASCADE)

    def calculate_days(self):
        # Logic to calculate days between start_date and end_date of absence_request
        start_date = self.absence_request.start_date
        end_date = self.absence_request.end_date
        return [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

    def __str__(self):
        return f"Days requested for {self.absence_request}"






