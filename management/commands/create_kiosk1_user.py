from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from login.models import Employee


class Command(BaseCommand):
    help = 'Creates a temporary user'

    def handle(self, *args, **options):
        if not Employee.objects.filter(username='Kiosk1').exists():
            Employee.objects.create(
                username='Kiosk1',
                password=make_password('freestand1'),
                name='Kiosk User',  # Add a default name
                role='Kiosk',  # Add a default role
                clock_number='1234'  # Add a default clock number
            )
            self.stdout.write(self.style.SUCCESS('Successfully created user Kiosk1'))
        else:
            self.stdout.write('User Kiosk1 already exists')
