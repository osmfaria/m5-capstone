# Generated by Django 4.1.1 on 2022-09-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0003_alter_schedule_court_alter_schedule_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="datetime",
            field=models.DateTimeField(unique=True),
        ),
    ]