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
        admin_clock_number = "001"
        Employee.objects.create_superuser(
            username=admin_username,
            name=admin_name,
            role="admin",
            clock_number=admin_clock_number,
            password="adminpass123",
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded database with employees")
        )
