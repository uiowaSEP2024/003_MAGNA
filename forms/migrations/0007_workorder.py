# Generated by Django 4.2.8 on 2024-03-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0006_alter_absencerequest_approval_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkOrder",
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
                ("order_number", models.CharField(max_length=255)),
                ("shift_number", models.CharField(max_length=100)),
                ("department_affected", models.CharField(max_length=100)),
                ("full_name", models.CharField(max_length=255)),
                ("machine_affected", models.CharField(max_length=255)),
                ("quality_issue", models.BooleanField(default=False)),
                ("safety_issue", models.BooleanField(default=False)),
                ("planned", models.BooleanField(default=False)),
                ("sensor_issue", models.BooleanField(default=False)),
                ("work_type", models.CharField(max_length=255)),
                ("requested_date", models.DateField()),
                ("operation_affected", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("describe_problem", models.TextField()),
                ("root_cause", models.TextField()),
                ("work_requested", models.TextField()),
            ],
            options={
                "db_table": "forms_work_order",
            },
        ),
    ]
