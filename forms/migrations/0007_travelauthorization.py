# Generated by Django 4.2.11 on 2024-03-24 21:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("forms", "0006_alter_absencerequest_approval_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="TravelAuthorization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clock_number", models.IntegerField()),
                ("name", models.CharField(max_length=100)),
                (
                    "department",
                    models.CharField(
                        choices=[("hr", "HR"), ("floor_staff", "Floor Staff")],
                        max_length=20,
                    ),
                ),
                ("destination", models.CharField(max_length=50)),
                ("departure_date", models.DateField()),
                ("return_date", models.DateField()),
                ("personal_car", models.BooleanField()),
                ("company_car", models.BooleanField()),
                ("car_rental", models.BooleanField()),
                ("airfare", models.BooleanField()),
                ("nights_lodging", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("signature", models.CharField(max_length=100)),
                (
                    "approval_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "department_manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
