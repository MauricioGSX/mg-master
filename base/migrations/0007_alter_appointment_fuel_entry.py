# Generated by Django 5.0.4 on 2024-09-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_appointment_fuel_entry_damageposition_vehiclephoto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="fuel_entry",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
