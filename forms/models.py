from datetime import date  # Import date directly

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.datetime_safe import datetime

from login.models import Employee


# Model for the AbsenceRequest form to keep track of all information
class AbsenceRequest(models.Model):
    """Model for the absence request form"""

    clock_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    approval_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="pending",
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
    email_address = models.EmailField()
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

    def clean(self):
        """Clean method for validation of approval status and shift number"""
        super().clean()
        approval_choice = dict(self._meta.get_field("approval_status").choices)
        shift_choices = dict(self._meta.get_field("shift_number").choices)

        if self.approval_status not in approval_choice:
            raise ValidationError({"approval_status": "Invalid approval."})
        if self.shift_number not in shift_choices:
            raise ValidationError({"shift_number": "Invalid shift number."})
        if not isinstance(self.end_date, date) or not isinstance(self.start_date, date):
            raise ValidationError("Start and end date must be a date.")
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after the start date.")
        if self.hours_gone < 0:
            raise ValidationError("Hours gone must be greater than 0.")
        if self.absence_type == "":
            raise ValidationError("Absence type cannot be empty.")

    def save(self, *args, **kwargs):
        """Overridden clean method in order to ensure clean method is run"""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        # Set the table name
        db_table = "forms_absence_request"


# Model for the WorkOrder form
class WorkOrder(models.Model):
    order_number = models.IntegerField()
    shift_number = models.CharField(max_length=100)
    department_affected = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    machine_affected = models.CharField(max_length=255)
    quality_issue = models.BooleanField(default=False)
    safety_issue = models.BooleanField(default=False)
    planned = models.BooleanField(default=False)
    sensor_issue = models.BooleanField(default=False)
    work_type = models.CharField(max_length=255)
    requested_date = models.DateField()
    operation_affected = models.CharField(max_length=255)
    email = models.EmailField()
    describe_problem = models.TextField()
    root_cause = models.TextField()
    work_requested = models.TextField()

    def clean(self):
        # Check if at least one checkbox is checked
        if not any([self.quality_issue, self.safety_issue, self.planned, self.sensor_issue]):
            raise ValidationError('At least one issue type must be selected.')

        # Here you can add more validation if needed

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Work Order #{self.order_number} by {self.full_name}"

    class Meta:
        # Set the table name
        db_table = "forms_work_order"


class AbsentDaysAllowed(models.Model):
    """Model for the allowed absent days on the calendar"""

    shiftDay = models.DateField(unique=True)  # Ensures each date is only entered once
    allowedAbsent = models.IntegerField(default=0)

    def __str__(self):
        """Return a string representing the shift schedule"""
        return f"{self.shiftDay}: {self.allowedAbsent} allowed absents"

    class Meta:
        """Meta class for the AbsentDaysAllowed model."""

        db_table = "absent_days_allowed"


class JobPDFs(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "job_posting_pdfs"