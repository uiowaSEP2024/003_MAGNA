# Generated by Django 4.2.10 on 2024-03-20 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0010_absencerequest_email_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpdfs",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
