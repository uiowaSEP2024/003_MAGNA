# Generated by CodiumAI

from forms.models import TravelAuthorization

import pytest

from login.models import Employee


class TestTravelAuthorization:



    #  Can create a valid travel authorization with all fields filled
    @pytest.mark.django_db
    def test_valid_travel_authorization_creation_all_fields(self):
        manager = Employee.objects.create(
            clock_number="123456",
            name="Manager Name",
            role="Manager",
            username='manager',
            password="testPass",
        )
        ta = TravelAuthorization.objects.create(
            clock_number=12345,
            name="John Doe",
            department="hr",
            destination="New York",
            departure_date="2022-01-01",
            return_date="2022-01-05",
            personal_car=True,
            company_car=False,
            car_rental=True,
            airfare=False,
            nights_lodging=4,
            department_manager=manager,
            email="test@example.com",
            signature="John Doe",
            approval_status="pending"
        )
        assert ta.clock_number == 12345
        assert ta.name == "John Doe"
        assert ta.department == "hr"
        assert ta.destination == "New York"
        assert ta.departure_date == "2022-01-01"
        assert ta.return_date == "2022-01-05"
        assert ta.personal_car == True
        assert ta.company_car == False
        assert ta.car_rental == True
        assert ta.airfare == False
        assert ta.nights_lodging == 4
        assert ta.department_manager == manager
        assert ta.email == "test@example.com"
        assert ta.signature == "John Doe"
        assert ta.approval_status == "pending"

    #  Can create a travel authorization with the minimum required fields
    @pytest.mark.django_db
    def test_create_travel_authorization_minimum_fields(self):
        manager = Employee.objects.create(
            clock_number="123456",
            name="Manager Name",
            role="Manager",
            username='manager',
            password="testPass",
        )
        ta = TravelAuthorization.objects.create(
            clock_number=12345,
            name="John Doe",
            department="hr",
            destination="New York",
            departure_date="2022-01-01",
            return_date="2022-01-05",
            department_manager=manager,
            nights_lodging=4,
            email="test@example.com",
            signature="John Doe"
        )
        assert ta.clock_number == 12345
        assert ta.name == "John Doe"
        assert ta.department == "hr"
        assert ta.destination == "New York"
        assert ta.departure_date == "2022-01-01"
        assert ta.return_date == "2022-01-05"
        assert ta.personal_car == False
        assert ta.company_car == False
        assert ta.car_rental == False
        assert ta.airfare == False
        assert ta.nights_lodging == 4
        assert ta.department_manager == manager
        assert ta.email == "test@example.com"
        assert ta.signature == "John Doe"
        assert ta.approval_status == "pending"

    #  Can create a travel authorization with only personal car selected
    @pytest.mark.django_db
    def test_create_travel_authorization_personal_car_only(self):
        manager = Employee.objects.create(
            clock_number="123456",
            name="Manager Name",
            role="Manager",
            username='manager',
            password="testPass",
        )
        ta = TravelAuthorization.objects.create(
            clock_number=12345,
            name="John Doe",
            department="hr",
            destination="New York",
            departure_date="2022-01-01",
            return_date="2022-01-05",
            personal_car=True,
            nights_lodging=4,
            department_manager=manager,
            email="test@example.com",
            signature="John Doe"
        )
        assert ta.clock_number == 12345
        assert ta.name == "John Doe"
        assert ta.department == "hr"
        assert ta.destination == "New York"
        assert ta.departure_date == "2022-01-01"
        assert ta.return_date == "2022-01-05"
        assert ta.personal_car == True
        assert ta.company_car == False
        assert ta.car_rental == False
        assert ta.airfare == False
        assert ta.nights_lodging == 4
        assert ta.department_manager == manager
        assert ta.email == "test@example.com"
        assert ta.signature == "John Doe"
        assert ta.approval_status == "pending"

    #  Cannot create a travel authorization with an invalid department
    @pytest.mark.django_db
    def test_invalid_department_travel_authorization_creation(self):
        manager = Employee.objects.create(
            clock_number="123456",
            name="Manager Name",
            role="Manager",
            username='manager',
            password="testPass",
        )
        with pytest.raises(ValueError):
            TravelAuthorization.objects.create(
                clock_number=12345,
                name="John Doe",
                department="invalid_department",
                destination="New York",
                departure_date="2022-01-01",
                return_date="2022-01-05",
                personal_car=True,
                nights_lodging=4,
                department_manager=manager,
                email="test@example.com",
                signature="John Doe",
                approval_status="pending"
            )

    #  Creating a travel authorization with an empty name field should raise an error.
    @pytest.mark.django_db
    def test_empty_name_travel_authorization_creation(self):
        manager = Employee.objects.create(
            clock_number="123456",
            name="Manager Name",
            role="Manager",
            username='manager',
            password="testPass",
        )
        with pytest.raises(ValueError):
            TravelAuthorization.objects.create(
                clock_number=12345,
                name="",
                department="hr",
                destination="New York",
                departure_date="2022-01-01",
                return_date="2022-01-05",
                personal_car=True,
                nights_lodging=4,
                department_manager=manager,
                email="test@example.com",
                signature="John Doe",
                approval_status="pending"
            )

    #  Creating a travel authorization with an invalid email should raise an error.
    @pytest.mark.django_db
    def test_invalid_email_travel_authorization_creation(self):
        manager = Employee.objects.create(
            clock_number="123456",
            name="Manager Name",
            role="Manager",
            username='manager',
            password="testPass",
        )
        with pytest.raises(ValueError):
            TravelAuthorization.objects.create(
                clock_number=12345,
                name="John Doe",
                department="hr",
                destination="New York",
                departure_date="2022-01-01",
                return_date="2022-01-05",
                personal_car=True,
                nights_lodging=4,
                department_manager=manager,
                email="invalid_email",
                signature="John Doe",
                approval_status="pending"
            )
