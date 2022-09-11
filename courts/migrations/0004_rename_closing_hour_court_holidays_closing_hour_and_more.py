# Generated by Django 4.1.1 on 2022-09-09 14:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("courts", "0003_court_closing_hour_court_opening_hour"),
    ]

    operations = [
        migrations.RenameField(
            model_name="court",
            old_name="closing_hour",
            new_name="holidays_closing_hour",
        ),
        migrations.RenameField(
            model_name="court",
            old_name="opening_hour",
            new_name="holidays_opening_hour",
        ),
        migrations.AddField(
            model_name="court",
            name="weekdays_closing_hour",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="court",
            name="weekdays_opening_hour",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="court",
            name="weekends_closing_hour",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="court",
            name="weekends_opening_hour",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="NonOperatingDays",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "regular_day_off",
                    models.CharField(
                        choices=[
                            ("MONDAY", "Monday"),
                            ("TUESDAY", "Tuesday"),
                            ("WEDNESDAY", "Wednesday"),
                            ("THURSDAY", "Thursday"),
                            ("FRIDAY", "Friday"),
                            ("SATURDAY", "Saturday"),
                            ("SUNDAY", "Sunday"),
                            ("DEFAULT", "Default"),
                        ],
                        default="DEFAULT",
                        max_length=9,
                    ),
                ),
                ("holidays", models.DateField(blank=True, null=True)),
                (
                    "court",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="non_operating_days",
                        to="courts.court",
                    ),
                ),
            ],
        ),
    ]
