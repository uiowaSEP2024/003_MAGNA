from django.db import models


class Workflow(models.Model):
    """Model representing a workflow."""

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("manager_review", "Manager Review"),
        ("HR_review", "HR Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="submitted"
    )

class FormEmailSetting(models.Model):
    form_type = models.CharField(max_length=100, unique=True)
    email_recipients = models.TextField(help_text="Comma-separated list of email addresses")

    def __str__(self):
        return self.form_type