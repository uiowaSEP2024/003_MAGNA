from django.db import models


class Employee(models.Model):
    """Model for employees"""

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    clock_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
