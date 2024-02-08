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

    @pytest.mark.django_db
    def test_employee_creation(self):
        """Test employee creation model"""
        employee = Employee.objects.create(
            name="Test User",
            role="employee",
            clock_number="021456",
            email="test@example.com",
        )
        assert employee.name == "Test User"
        assert employee.role == "Developer"
        assert employee.clock_number == "12345"
        assert employee.email == "test@example.com"
