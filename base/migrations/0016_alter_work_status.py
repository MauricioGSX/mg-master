# Generated by Django 5.0.4 on 2024-10-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0015_alter_work_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="work",
            name="status",
            field=models.CharField(
                choices=[
                    ("En progreso", "En progreso"),
                    ("Esperando Repuestos", "Esperando Repuestos"),
                    ("Completado", "Completado"),
                ],
                default="En progreso",
                max_length=50,
            ),
        ),
    ]