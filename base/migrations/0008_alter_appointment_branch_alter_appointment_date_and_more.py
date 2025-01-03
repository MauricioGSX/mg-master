# Generated by Django 5.0.4 on 2024-09-30 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_alter_appointment_fuel_entry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="branch",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.branch",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="fuel_entry",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="mechanic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.mechanic",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="service",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.service",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="time",
            field=models.CharField(
                blank=True,
                choices=[("AM", "AM"), ("PM", "PM")],
                default="AM",
                max_length=2,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="vehicle",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.vehicle",
            ),
        ),
    ]
