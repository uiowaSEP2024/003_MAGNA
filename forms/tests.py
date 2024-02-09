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
