# Generated by CodiumAI

import datetime
from unittest.mock import MagicMock

import pytest
from django.http import HttpRequest, JsonResponse

from forms.models import AbsenceRequest
from forms.views import search_requests
from login.models import Employee


class TestSearchRequests:
    """Contains tests for the requests view."""

    @pytest.fixture
    def setup(self):
        """Creates two employees in the database."""
        Employee.objects.create(
            username="johndoe",
            password="password",
            clock_number="12345",
            name="John Doe",
            role="Manager",
            email="johndoe@email.com",
        )
        Employee.objects.create(
            username="janedoe",
            password="password",
            clock_number="54321",
            name="Jane Doe",
            role="Manager",
            email="janedoe@email.com",
        )
        Employee.objects.create(
            username="kiosk",
            password="password",
            clock_number="111111",
            name="kiosk",
            role="kiosk",
            email="kiosk@email",
        )

        request = HttpRequest()
        request.user = Employee.objects.get(name="kiosk")
        return request

    @pytest.mark.django_db
    def test_matching_requests(self, setup):
        """Returns a JsonResponse object with a list of absence requests matching the clock number."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value="12345")

        matching_requests = [
            AbsenceRequest(
                start_date=datetime.date(2022, 1, 1),
                end_date=datetime.date(2022, 1, 5),
                filled_by=Employee.objects.get(name="John Doe"),
                approval=Employee.objects.get(name="Jane Doe"),
                approval_status="Approved",
                absence_type="Vacation",
            ),
            AbsenceRequest(
                start_date=datetime.date(2022, 2, 1),
                end_date=datetime.date(2022, 2, 5),
                filled_by=Employee.objects.get(name="John Doe"),
                approval=Employee.objects.get(name="Jane Doe"),
                approval_status="Approved",
                absence_type="Sick Leave",
            ),
        ]
        AbsenceRequest.objects.filter = MagicMock(return_value=matching_requests)

        # Act
        response = search_requests(request)

        # Assert
        expected_data = [
            {
                "start_date": "2022-01-01",
                "end_date": "2022-01-05",
                "filled_by": "John Doe",
                "approval": "Jane Smith",
                "approval_status": "Approved",
                "absence_type": "Vacation",
            },
            {
                "start_date": "2022-02-01",
                "end_date": "2022-02-05",
                "filled_by": "John Doe",
                "approval": "Jane Smith",
                "approval_status": "Approved",
                "absence_type": "Sick Leave",
            },
        ]
        assert response == JsonResponse(expected_data, safe=False)

    @pytest.mark.django_db
    def test_no_clock_number(self, setup):
        """Returns an empty JsonResponse object if no clock number is provided."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value=None)

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    @pytest.mark.django_db
    def test_filter_by_clock_number(self, setup):
        """Filters absence requests by clock number."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value="12345")
        matching_requests = [
            AbsenceRequest(
                start_date=datetime.date(2022, 1, 1),
                end_date=datetime.date(2022, 1, 5),
                filled_by=Employee.objects.get(name="John Doe"),
                approval=Employee.objects.get(name="Jane Doe"),
                approval_status="Approved",
                absence_type="Vacation",
            ),
            AbsenceRequest(
                start_date=datetime.date(2022, 2, 1),
                end_date=datetime.date(2022, 2, 5),
                filled_by=Employee.objects.get(name="John Doe"),
                approval=Employee.objects.get(name="Jane Doe"),
                approval_status="Approved",
                absence_type="Sick Leave",
            ),
        ]
        AbsenceRequest.objects.filter = MagicMock(return_value=matching_requests)

        # Act
        search_requests(request)

        # Assert
        AbsenceRequest.objects.filter.assert_called_once_with(clock_number="12345")

    @pytest.mark.django_db
    def test_absence_requests_data(self, setup):
        """Returns a JsonResponse object with absence requests data."""

        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value="12345")
        matching_requests = [
            AbsenceRequest(
                start_date=datetime.date(2022, 1, 1),
                end_date=datetime.date(2022, 1, 5),
                filled_by=Employee.objects.get(name="John Doe"),
                approval=Employee.objects.get(name="Jane Doe"),
                approval_status="Approved",
                absence_type="Vacation",
            ),
            AbsenceRequest(
                start_date=datetime.date(2022, 2, 1),
                end_date=datetime.date(2022, 2, 5),
                filled_by=Employee.objects.get(name="John Doe"),
                approval=Employee.objects.get(name="Jane Doe"),
                approval_status="Approved",
                absence_type="Sick Leave",
            ),
        ]
        AbsenceRequest.objects.filter = MagicMock(return_value=matching_requests)

        # Act
        response = search_requests(request)

        # Assert
        expected_data = [
            {
                "start_date": "2022-01-01",
                "end_date": "2022-01-05",
                "filled_by": "John Doe",
                "approval": "Jane Smith",
                "approval_status": "Approved",
                "absence_type": "Vacation",
            },
            {
                "start_date": "2022-02-01",
                "end_date": "2022-02-05",
                "filled_by": "John Doe",
                "approval": "Jane Smith",
                "approval_status": "Approved",
                "absence_type": "Sick Leave",
            },
        ]
        assert response == JsonResponse(expected_data, safe=False)

    @pytest.mark.django_db
    def test_not_get_request(self, setup):
        """Returns a JsonResponse object with an empty list if the request method is not GET."""
        # Arrange
        request = setup
        request.method = "POST"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    @pytest.mark.django_db
    def test_not_kiosk_role(self, setup):
        """Returns a JsonResponse object with an empty list if the user role is not kiosk."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "admin"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    @pytest.mark.django_db
    def test_no_clock_number_provided(self, setup):
        """Returns an empty JsonResponse object if no clock number is provided."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value=None)

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    @pytest.mark.django_db
    def test_no_matching_requests(self, setup):
        """Returns an empty JsonResponse object if no absence requests match the clock number."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value="12345")
        AbsenceRequest.objects.filter = MagicMock(return_value=[])

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    @pytest.mark.django_db
    def test_not_get_request_empty_list(self, setup):
        """Returns a JsonResponse object with an empty list if the request method is not GET."""
        # Arrange
        request = setup
        request.method = "POST"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    @pytest.mark.django_db
    def test_not_kiosk_role_empty_list(self, setup):
        """Returns a JsonResponse object with an empty list if the user role is not kiosk."""
        # Arrange
        request = setup
        request.method = "GET"
        request.user.role = "admin"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)
