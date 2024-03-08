# Generated by CodiumAI

import datetime
from unittest.mock import MagicMock

import pytest
from django.http import HttpRequest, JsonResponse

from forms.models import AbsenceRequest
from forms.views import search_requests
from login.models import Employee


class TestSearchRequests:
    @pytest.fixture
    def setup_data(self):
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
            clock_number="12345",
            name="Jane Doe",
            role="Manager",
            email="janedoe@email.com",
        )

    #  Returns a JsonResponse object with a list of absence requests matching the clock number.
    @pytest.mark.django_db
    def test_matching_requests(self, setup_data):
        # Arrange
        request = HttpRequest()
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

    #  Returns an empty JsonResponse object if no clock number is provided.
    @pytest.mark.django_db
    def test_no_clock_number(self, setup_data):
        # Arrange
        request = HttpRequest()
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value=None)

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    #  Filters absence requests by clock number.
    @pytest.mark.django_db
    def test_filter_by_clock_number(self, setup_data):
        # Arrange
        request = HttpRequest()
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

    #  Returns a JsonResponse object with absence requests data.
    @pytest.mark.django_db
    def test_absence_requests_data(self, setup_data):

        # Arrange
        request = HttpRequest()
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

    #  Returns an empty JsonResponse object if the request method is not GET.
    @pytest.mark.django_db
    def test_not_get_request(self):
        # Arrange
        request = HttpRequest()
        request.method = "POST"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    #  Returns an empty JsonResponse object if the user role is not kiosk.
    @pytest.mark.django_db
    def test_not_kiosk_role(self):
        # Arrange
        request = HttpRequest()
        request.method = "GET"
        request.user.role = "admin"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    #  Returns an empty JsonResponse object if the clock number is not provided.
    @pytest.mark.django_db
    def test_no_clock_number_provided(self):
        # Arrange
        request = HttpRequest()
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value=None)

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    #  Returns an empty JsonResponse object if no absence requests match the clock number.
    @pytest.mark.django_db
    def test_no_matching_requests(self):
        # Arrange
        request = HttpRequest()
        request.method = "GET"
        request.user.role = "kiosk"
        request.GET.get = MagicMock(return_value="12345")
        AbsenceRequest.objects.filter = MagicMock(return_value=[])

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    #  Returns a JsonResponse object with an empty list if the request method is not GET.
    @pytest.mark.django_db
    def test_not_get_request_empty_list(self):
        # Arrange
        request = HttpRequest()
        request.method = "POST"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)

    #  Returns a JsonResponse object with an empty list if the user role is not kiosk.
    @pytest.mark.django_db
    def test_not_kiosk_role_empty_list(self):
        # Arrange
        request = HttpRequest()
        request.method = "GET"
        request.user.role = "admin"

        # Act
        response = search_requests(request)

        # Assert
        assert response == JsonResponse([], safe=False)
