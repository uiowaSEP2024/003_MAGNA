import django.core.exceptions
from cfgv import ValidationError
from django.test import TestCase

from forms.models import AbsenceRequest
from login.models import Employee


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

    def test_valid_absence_request_creation(self):
        """Test for valid absence request creation"""

        ar = AbsenceRequest.objects.create(
            start_date="2024-02-08",
            end_date="2024-02-10",
            approval_status="pending",
            shift_number="1st",
            hours_gone=16,
            absence_type="vacation",
            approval=self.manager,
            filled_by=self.floor,
        )
        self.assertEqual(ar.start_date, "2024-02-08")
        self.assertEqual(ar.end_date, "2024-02-10")
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
                start_date="2024/02/08",
                end_date="2024/02/10",
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
            start_date="2024-02-08",
            end_date="2024-02-10",
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
            start_date="2024-02-08",
            end_date="2024-02-10",
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
            start_date="2024-02-08",
            end_date="2024-02-10",
            approval_status="not valid",
            shift_number="1st",
            hours_gone=16,
            absence_type="vacation",
            approval=self.manager,
            filled_by=self.floor,
        )
