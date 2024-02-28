from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Creates a Kiosk1 user'

    def handle(self, *args, **options):
        if not Employee.objects.filter(username='Kiosk1').exists():
            Employee.objects.create(username='Kiosk1', password=make_password('freestand1'))
            self.stdout.write(self.style.SUCCESS('Successfully created user Kiosk1'))
        else:
            self.stdout.write('User Kiosk1 already exists')
