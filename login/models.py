from django.db import models


class Employee(models.Model):
    """Model for employees"""

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    clock_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    def clean(self):
        """Clean method for validation of approval status and shift number"""
        super().clean()

    def save(self, *args, **kwargs):
        """Overridden clean method in order to ensure clean method is run"""
        self.full_clean()
        super().save(*args, **kwargs)
