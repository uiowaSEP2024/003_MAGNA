import pytest
from django.test import TestCase
from django.urls import reverse

from login.models import Employee


class LoginTestCase(TestCase):
    """FILL IN"""

    def test_login_page(self):
        """FILL IN"""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_login_form(self):
        """FILL IN"""
        # Add a test for form submission here
        pass


class EmployeeModelTestCase(TestCase):
    """Testing class for the employee model"""

    def test_employee_creation(self):
        employee = Employee.objects.create(
            name="John Doe",
            role="Developer",
            clock_number="123456",
            email="john@example.com",
        )
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.role, "Developer")
        self.assertEqual(employee.clock_number, "123456")
        self.assertEqual(employee.email, "john@example.com")
