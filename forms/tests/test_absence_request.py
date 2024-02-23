# Generated by CodiumAI
import datetime

import pytest
from django.core.exceptions import ValidationError

from forms.models import AbsenceRequest
from login.models import Employee


class TestAbsenceRequest:
    """Testing class for Absence Request model"""

    @pytest.mark.django_db
    def test_create_new_absence_request(self):
        """Creating a new AbsenceRequest object with valid data and saving it should create a new record in the database."""  # noqa: E501
        absence_request = AbsenceRequest(
            start_date="2022-01-01",
            end_date="2022-01-02",
            approval_status="pending",
            shift_number="1st",
            hours_gone=8,
            absence_type="Vacation",
        )
        absence_request.save()

        assert AbsenceRequest.objects.count() == 1
        assert AbsenceRequest.objects.first() == absence_request

    @pytest.mark.django_db
    def test_invalid_start_date(self):
        """Creating a new AbsenceRequest object with an invalid start_date should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            absence_request = AbsenceRequest(
                start_date="2022-01-32",
                end_date="2022-01-02",
                approval_status="pending",
                shift_number="1st",
                hours_gone=8,
                absence_type="Vacation",
            )
            absence_request.full_clean()

    @pytest.mark.django_db
    def test_clean_method_with_valid_data(self):
        """Calling the clean() method on an AbsenceRequest object with valid data should not raise any exceptions."""  # noqa: E501
        absence_request = AbsenceRequest(
            start_date="2022-01-01",
            end_date="2022-01-05",
            approval_status="pending",
            shift_number="1st",
            hours_gone=40,
            absence_type="Vacation",
        )
        try:
            absence_request.full_clean()
        except ValidationError:
            pytest.fail("ValidationError raised unexpectedly")

    @pytest.mark.django_db
    def test_delete_absence_request(self):
        """Deleting an existing AbsenceRequest object should remove the corresponding record from the database."""  # noqa: E501
        # Create a new AbsenceRequest object
        absence_request = AbsenceRequest.objects.create(
            start_date="2022-01-01",
            end_date="2022-01-05",
            approval_status="pending",
            shift_number="1st",
            hours_gone=40,
            absence_type="Vacation",
        )

        # Get the initial count of AbsenceRequest objects in the database
        initial_count = AbsenceRequest.objects.count()

        # Delete the AbsenceRequest object
        absence_request.delete()

        # Get the final count of AbsenceRequest objects in the database
        final_count = AbsenceRequest.objects.count()

        # Assert that the final count is less than the initial count
        assert final_count < initial_count

    @pytest.mark.django_db
    def test_save_valid_data(self):
        """Calling the save() method on an AbsenceRequest object with valid data should save the object to the database."""  # noqa: E501
        # Create a valid AbsenceRequest object
        absence_request = AbsenceRequest(
            start_date="2022-01-01",
            end_date="2022-01-05",
            approval_status="pending",
            shift_number="1st",
            hours_gone=40,
            absence_type="Vacation",
        )

        # Save the object
        absence_request.save()

        # Retrieve the object from the database
        saved_absence_request = AbsenceRequest.objects.get(id=absence_request.id)

        # Assert that the retrieved object is the same as the saved object
        assert saved_absence_request == absence_request

    @pytest.mark.django_db
    def test_update_existing_absence_request(self):
        """Updating an existing AbsenceRequest object with valid data and saving it should update the corresponding record in the database."""  # noqa: E501
        # Create an AbsenceRequest object
        absence_request = AbsenceRequest.objects.create(
            start_date="2022-01-01",
            end_date="2022-01-05",
            approval_status="pending",
            shift_number="1st",
            hours_gone=40,
            absence_type="Vacation",
        )

        # Update the AbsenceRequest object with valid data
        absence_request.start_date = "2022-02-01"
        absence_request.end_date = "2022-02-05"
        absence_request.approval_status = "approved"
        absence_request.shift_number = "2nd"
        absence_request.hours_gone = 32
        absence_request.absence_type = "Sick Leave"

        # Save the updated AbsenceRequest object
        absence_request.save()

        # Retrieve the updated AbsenceRequest object from the database
        updated_absence_request = AbsenceRequest.objects.get(id=absence_request.id)

        # Check if the updated fields match the updated values
        assert updated_absence_request.start_date == datetime.date(2022, 2, 1)
        assert updated_absence_request.end_date == datetime.date(2022, 2, 5)
        assert updated_absence_request.approval_status == "approved"
        assert updated_absence_request.shift_number == "2nd"
        assert updated_absence_request.hours_gone == 32
        assert updated_absence_request.absence_type == "Sick Leave"

    @pytest.mark.django_db
    def test_update_approval_id_field(self):
        """Setting the approval field of an AbsenceRequest object to a valid Employee object and saving it should update the approval_id field in the corresponding record in the database."""  # noqa: E501
        # Create a valid Employee object
        employee = Employee.objects.create(name="John Doe")

        # Create an AbsenceRequest object
        absence_request = AbsenceRequest.objects.create(
            start_date="2022-01-01",
            end_date="2022-01-05",
            approval_status="pending",
            shift_number="1st",
            hours_gone=40,
            absence_type="Vacation",
            filled_by=employee,
        )

        # Set the approval field to the valid Employee object
        absence_request.approval = employee

        # Save the AbsenceRequest object
        absence_request.save()

        # Retrieve the updated AbsenceRequest object from the database
        updated_absence_request = AbsenceRequest.objects.get(id=absence_request.id)

        # Check if the approval_id field is updated with the correct value
        assert updated_absence_request.approval_id == employee.id

    @pytest.mark.django_db
    def test_update_filled_by_id(self):
        """Setting the filled_by field of an AbsenceRequest object to a valid Employee object and saving it should update the filled_by_id field in the corresponding record in the database."""  # noqa: E501
        # Create a valid Employee object
        employee = Employee.objects.create(name="John Doe")

        # Create an AbsenceRequest object
        absence_request = AbsenceRequest.objects.create(
            start_date="2022-01-01",
            end_date="2022-01-02",
            approval_status="pending",
            shift_number="1st",
            hours_gone=8,
            absence_type="Sick Leave",
        )

        # Set the filled_by field to the valid Employee object
        absence_request.filled_by = employee

        # Save the AbsenceRequest object
        absence_request.save()

        # Retrieve the updated AbsenceRequest object from the database
        updated_absence_request = AbsenceRequest.objects.get(id=absence_request.id)

        # Check if the filled_by_id field is updated with the correct value
        assert updated_absence_request.filled_by_id == employee.id

    @pytest.mark.django_db
    def test_invalid_end_date(self):
        """Creating a new AbsenceRequest object with an invalid end_date should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            AbsenceRequest.objects.create(
                start_date="2022-01-01",
                end_date="2021-12-31",
                approval_status="pending",
                shift_number="1st",
                hours_gone=8,
                absence_type="Vacation",
                filled_by=None,
                approval=None,
            )

    @pytest.mark.django_db
    def test_invalid_approval_status(self):
        """Creating a new AbsenceRequest object with an invalid approval_status should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            AbsenceRequest.objects.create(
                start_date="2022-01-01",
                end_date="2022-01-02",
                approval_status="invalid",
                shift_number="1st",
                hours_gone=8,
                absence_type="Sick Leave",
            )

    @pytest.mark.django_db
    def test_invalid_shift_number(self):
        """Creating a new AbsenceRequest object with an invalid shift_number should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            AbsenceRequest.objects.create(
                start_date="2022-01-01",
                end_date="2022-01-02",
                approval_status="pending",
                shift_number="invalid_shift",
                hours_gone=8,
                absence_type="Sick Leave",
                filled_by=None,
                approval=None,
            )

    @pytest.mark.django_db
    def test_invalid_hours_gone(self):
        """Creating a new AbsenceRequest object with an invalid hours_gone should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            absence_request = AbsenceRequest(
                start_date="2022-01-01",
                end_date="2022-01-02",
                approval_status="pending",
                shift_number="1st",
                hours_gone=-10,
                absence_type="Sick Leave",
            )
            absence_request.full_clean()

    @pytest.mark.django_db
    def test_null_approval_field(self):
        """Creating a new AbsenceRequest object with a null approval field should not raise a ValidationError."""  # noqa: E501
        absence_request = AbsenceRequest(
            start_date="2022-01-01",
            end_date="2022-01-02",
            approval_status="pending",
            shift_number="1st",
            hours_gone=8,
            absence_type="Vacation",
            filled_by=None,
            approval=None,
        )
        try:
            absence_request.full_clean()
        except ValidationError:
            self.fail("ValidationError raised when approval field is null")

    @pytest.mark.django_db
    def test_create_absence_request_with_null_filled_by(self):
        """Creating a new AbsenceRequest object with a null filled_by field should not raise a ValidationError."""  # noqa: E501
        absence_request = AbsenceRequest(
            start_date="2022-01-01",
            end_date="2022-01-02",
            approval_status="pending",
            shift_number="1st",
            hours_gone=8,
            absence_type="Sick Leave",
            filled_by=None,
        )
        absence_request.save()
        assert absence_request.id is not None

    @pytest.mark.django_db
    def test_start_date_after_end_date(self):
        """Creating a new AbsenceRequest object with a start_date that is after the end_date should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            absence_request = AbsenceRequest(
                start_date="2022-1-1", end_date="2021-12-31"
            )
            absence_request.full_clean()

    @pytest.mark.django_db
    def test_negative_hours_gone(self):
        """Creating a new AbsenceRequest object with an hours_gone value that is negative should raise a ValidationError."""  # noqa: E501
        with pytest.raises(ValidationError):
            absence_request = AbsenceRequest(hours_gone=-10)
            absence_request.full_clean()

    @pytest.mark.django_db
    def test_absence_request_with_long_absence_type(self):
        """Creating a new AbsenceRequest object with an absence_type that is longer than 50 characters should raise a ValidationError."""  # noqa: E501
        absence_type = "This is a very long absence type that exceeds the maximum limit of 50 characters"
        with pytest.raises(ValidationError):
            absence_request = AbsenceRequest(absence_type=absence_type)
            absence_request.full_clean()
