from django.db import models


class Workflow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('manager_review', 'Manager Review'),
        ('HR_review', 'HR Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
