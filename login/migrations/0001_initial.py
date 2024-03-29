# Generated by Django 4.2.8 on 2024-02-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("clock_number", models.CharField(max_length=10, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
