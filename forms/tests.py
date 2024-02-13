from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from forms.models import AbsenceRequest
from login.models import Employee


class AbsenceRequestTestCase(TestCase):
    """Testing class for absence request model"""

    def test_valid_absence_request_creation(self):
        """Test for valid absence request creation"""
        manager = Employee.objects.create(
            clock_number="123456",
            email="manager@email",
        )

        floor = Employee.objects.create(
            clock_number="654321",
            email="floor@email",
        )

        ar = AbsenceRequest.objects.create(
            start_date="2024-02-08",
            end_date="2024-02-10",
            approval_status="pending",
            shift_number="1st",
            hours_gone=16,
            absence_type="vacation",
            approval=manager,
            filled_by=floor,
        )
        self.assertEqual(ar.start_date, "2024-02-08")
        self.assertEqual(ar.end_date, "2024-02-10")
        self.assertEqual(ar.approval_status, "pending")
        self.assertEqual(ar.shift_number, "1st")
        self.assertEqual(ar.hours_gone, 16)
        self.assertEqual(ar.absence_type, "vacation")
        self.assertEqual(ar.approval, manager)
        self.assertEqual(ar.filled_by, floor)

    def setUp(self):
        # Setup initial valid and invalid form data
        self.valid_form_data = {
            'start_date': '2024-01-01',
            'end_date': '2024-01-05',
            'shift_number': '1st',
            'hours_gone': 8,
            'absence_type': 'vacation',
        }

        self.invalid_form_data = {
            # Example of invalid form data: missing 'end_date'
            'start_date': '2024-01-01',
            'shift_number': '1st',
            'hours_gone': 8,
            'absence_type': 'vacation',
        }

    def test_invalid_form_submission(self):
        # Submit the form via post with invalid data
        response = self.client.post(reverse('submit_absence_request'), self.invalid_form_data)

        # Check that no AbsenceRequest object was created
        self.assertEqual(AbsenceRequest.objects.count(), 0)

    def test_requests_page_content(self):
        # Create a test AbsenceRequest
        AbsenceRequest.objects.create(**self.valid_form_data)

        # Get the requests page
        response = self.client.get(reverse('requests'))

        # Check that the page loads (response code 200)
        self.assertEqual(response.status_code, 200)

        # Check that the context contains AbsenceRequest objects
        self.assertTrue('requests' in response.context)
        self.assertEqual(len(response.context['requests']), 1)