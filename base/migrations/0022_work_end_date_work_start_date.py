# Generated by Django 5.0.4 on 2024-10-17 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0021_vehicle_vin_delete_news"),
    ]

    operations = [
        migrations.AddField(
            model_name="work",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="work",
            name="start_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
