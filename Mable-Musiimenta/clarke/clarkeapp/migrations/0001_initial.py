# Generated by Django 5.0.6 on 2024-05-17 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Index",
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
                (
                    "first_name",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
                ("course", models.CharField(max_length=255)),
                ("entry_scheme", models.CharField(max_length=255)),
                ("intake", models.CharField(max_length=255)),
                ("sponsorship", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")],
                        default="male",
                        max_length=255,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("residence", models.CharField(max_length=255)),
            ],
        ),
    ]
