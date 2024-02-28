import pytest
import datetime

from forms.models import TravelAuthorization


class TestTravelAuthorization:

    @pytest.mark.django_db
    def test_create_new_travel_authorization(self):
        travel_auth = TravelAuthorization(
            clock_number=1,
            name="testy",
            department="hr",
            destination="Test, Florida",
            departure_date='2025-01-01',
            return_date='2025-01-04',
            personal_car=True,
            company_car=False,
            car_rental=False,
            airfare=True,
            nights_lodging=3,
            department_manager="example",
            email="test@test.com",
            signature="testy"
        )
        travel_auth.save()

        assert TravelAuthorization.objects.count() == 1
        assert TravelAuthorization.objects.first() == travel_auth