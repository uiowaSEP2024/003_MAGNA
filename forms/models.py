from datetime import date  # Import date directly

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
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


# Validators for travel auth go here
def check_mail(value):
    if "@" not in value:
        raise ValidationError("The email is not valid.")


class TravelAuthorization(models.Model):
    """The model for travel authorization forms"""
    clock_number = models.IntegerField()
    name = models.CharField(max_length=100)
    department = models.CharField(
        max_length=20, choices=[("hr", "HR"), ("floor_staff", "Floor Staff")]
    )
    destination = models.CharField(max_length=50)
    departure_date = models.DateField()
    return_date = models.DateField()
    personal_car = models.BooleanField(default=False)
    company_car = models.BooleanField(default=False)
    car_rental = models.BooleanField(default=False)
    airfare = models.BooleanField(default=False)
    nights_lodging = models.IntegerField()
    department_manager = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(validators=[validate_email])
    signature = models.CharField(max_length=100)
    approval_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="pending",
    )

    def clean(self):
        """A overrriden clean method so it actually gets called when the object is saved."""
        super().clean()

    def save(self, *args, **kwargs):
        """Overridden clean method in order to ensure clean method is run"""
        self.full_clean()
        super().save(*args, **kwargs)


# Validations and input stuff starts here
class DateInput(forms.DateInput):
    """To make sure the date input appears properly on the form, this was created."""
    input_type = "date"


class TravelAuthorizationForm(forms.ModelForm):
    """The model form for the travel auth form."""
    class Meta:
        model = TravelAuthorization
        fields = [
            "clock_number",
            "name",
            "department",
            "destination",
            "departure_date",
            "return_date",
            "personal_car",
            "company_car",
            "car_rental",
            "airfare",
            "nights_lodging",
            "department_manager",
            "email",
            "signature",
        ]
        widgets = {"departure_date": DateInput(), "return_date": DateInput()}


# Model to keep track of allowed absent days on the Calendar
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
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "job_posting_pdfs"