import random

from django.core.management.base import BaseCommand

from forms.models import AbsenceRequest
from login.models import Employee


class Command(BaseCommand):
    """Seeds the database with absence requests"""

    help = "Seeds the database with absence requests"

    def handle(self, *args, **options):
        """Handle method for seeding the database with absence requests"""
        shift_options = ["1st", "2nd", "3rd", "4th"]
        absence_type_options = ["sick", "vacation", "personal", "other"]
        approval_options = ["pending", "approved", "denied"]

        # Create absence requests
        for i in range(25):
            filled_by_employee = Employee.objects.get(id=random.randint(12, 41))
            AbsenceRequest.objects.create(
                start_date=f"2024-08-0{random.randint(1, 9)}",
                end_date=f"2024-08-{random.randint(1, 3)}0",
                shift_number=shift_options[random.randint(0, 3)],
                hours_gone=random.randint(1, 8),
                absence_type=absence_type_options[random.randint(0, 3)],
                approval_id=random.randint(2, 6),
                filled_by_id=filled_by_employee.id,
                clock_number=filled_by_employee.clock_number,
                approval_status=approval_options[random.randint(0, 2)],
            )

        self.stdout.write(
            self.style.SUCCESS("Seeded the database with absence requests")
        )
