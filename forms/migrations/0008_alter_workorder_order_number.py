# Generated by Django 4.2.8 on 2024-03-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0007_workorder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workorder",
            name="order_number",
            field=models.IntegerField(),
        ),
    ]
