import datetime

import django.core.exceptions
from cfgv import ValidationError
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from forms.models import AbsenceRequest
from login.models import Employee

from django.core import mail

class AbsenceRequestTestCase(TestCase):
    """Testing class for absence request model"""

    def setUp(self):
        self.manager = Employee.objects.create(
            clock_number="123456",
            email="manager@email",
        )

        self.floor = Employee.objects.create(
            clock_number="654321",
            email="floor@email",
        )

        self.valid_form_data = {
            "s_date": "2024-01-01",
            "e_date": "2024-01-05",
            "approval_status": "pending",
            "shift_number": "1st",
            "hours_gone": 8,
            "absence_type": "vacation",
        }

        self.invalid_form_data = {
            # Example of invalid form data: missing 'e_date'
            "s_date": "2024-01-01",
            "shift_number": "1st",
            "hours_gone": 8,
            "absence_type": "vacation",
        }

    def test_valid_absence_request_creation(self):
        """Test for valid absence request creation"""

        ar = AbsenceRequest.objects.create(
            s_date="2024-02-08",
            e_date="2024-02-10",
            approval_status="pending",
            shift_number="1st",
            hours_gone=16,
            absence_type="vacation",
            approval=self.manager,
            filled_by=self.floor,
        )
        self.assertEqual(ar.s_date, datetime.date(2024, 2, 8))
        self.assertEqual(ar.e_date, datetime.date(2024, 2, 10))
        self.assertEqual(ar.approval_status, "pending")
        self.assertEqual(ar.shift_number, "1st")
        self.assertEqual(ar.hours_gone, 16)
        self.assertEqual(ar.absence_type, "vacation")
        self.assertEqual(ar.approval, self.manager)
        self.assertEqual(ar.filled_by, self.floor)

    def test_invalid_absence_request_creation(self):
        """Test for invalid absence request creation"""
        with self.assertRaises(django.core.exceptions.ValidationError):
            # Providing invalid date format
            AbsenceRequest.objects.create(
                s_date="2024/02/08",
                e_date="2024/02/10",
                approval_status="pending",
                shift_number="1st",
                hours_gone=16,
                absence_type="vacation",
                approval=self.manager,
                filled_by=self.floor,
            )

    def test_approval_status_transition(self):
        """Test for approval status transition"""
        ar = AbsenceRequest.objects.create(
            s_date="2024-02-08",
            e_date="2024-02-10",
            approval_status="pending",
            shift_number="1st",
            hours_gone=16,
            absence_type="vacation",
            approval=self.manager,
            filled_by=self.floor,
        )

        # Simulate approval
        ar.approval_status = "approved"
        ar.save()
        self.assertEqual(ar.approval_status, "approved")

        # Simulate rejection
        ar.approval_status = "rejected"
        ar.save()
        self.assertEqual(ar.approval_status, "rejected")

        # Simulate pending
        ar.approval_status = "pending"
        ar.save()
        self.assertEqual(ar.approval_status, "pending")

    def test_invalid_shift_choice(self):
        """Test for raising error if invalid shift is given"""
        with self.assertRaises(django.core.exceptions.ValidationError):
            AbsenceRequest.objects.create(
                s_date="2024-02-08",
                e_date="2024-02-10",
                approval_status="pending",
                shift_number="invalid option",
                hours_gone=16,
                absence_type="vacation",
                approval=self.manager,
                filled_by=self.floor,
            )

    def test_invalid_approval_status(self):
        """Test for raising error if invalid approval status is given"""
        with self.assertRaises(django.core.exceptions.ValidationError):
            AbsenceRequest.objects.create(
                s_date="2024-02-08",
                e_date="2024-02-10",
                approval_status="not valid",
                shift_number="1st",
                hours_gone=16,
                absence_type="vacation",
                approval=self.manager,
                filled_by=self.floor,
            )

    def test_invalid_form_submission(self):
        """FILL IN"""
        # Submit the form via post with invalid data
        self.client.post(reverse("submit_absence_request"), self.invalid_form_data)

        # Check that no AbsenceRequest object was created
        self.assertEqual(AbsenceRequest.objects.count(), 0)

    def test_requests_page_content(self):
        """FILL IN"""
        # Create a test AbsenceRequest
        AbsenceRequest.objects.create(**self.valid_form_data)

        # Get the requests page
        response = self.client.get(reverse("requests"))

        # Check that the page loads (response code 200)
        self.assertEqual(response.status_code, 200)

        # Check that the context contains AbsenceRequest objects
        self.assertTrue("requests" in response.context)
        self.assertEqual(len(response.context["requests"]), 1)

class AbsenceRequestEmailTest(TestCase):
    def test_email_sent_on_valid_form_submission(self):
        response = self.client.post(reverse("submit_absence_request"), {
            "first_day_absent": "2024-02-14",
            "last_day_absent": "2024-02-15",
            "shift": "1st",
            "hours": "8",
            "absence_type": "sick",
            "email": "test@example.com",  # Update with the correct form field
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect occurs
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Absence Request Submitted')
        self.assertEqual(mail.outbox[0].to, ['test@example.com'])