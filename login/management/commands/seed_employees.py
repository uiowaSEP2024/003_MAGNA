from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from login.models import Employee


class Command(BaseCommand):
    """Seeds the database with employees"""

    help = "Seeds the database with employees"

    def handle(self, *args, **options):
        """Handle method for seeding the database with employees"""

        # Create a superuser
        admin_username = "admin"
        admin_name = "Admin"
        admin_clock_number = "0000"
        Employee.objects.create_superuser(
            username=admin_username,
            name=admin_name,
            role="admin",
            clock_number=admin_clock_number,
            password="adminpass123",
        )

        # Create manager employees
        for i in range(5):
            Employee.objects.create(
                username=f"manager{i+1}",
                name=f"Manager {i+1}",
                role="manager",
                clock_number=f"100{i+1}",
                password=f"managerpass{i+1}",
            )

        # Create HR employees
        for i in range(5):
            Employee.objects.create(
                username=f"hr{i+1}",
                name=f"HR Employee {i+1}",
                role="hr",
                clock_number=f"200{i+1}",
                password=f"hrpass{i+1}",
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded database with employees")
        )
