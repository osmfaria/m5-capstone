# Generated by Django 4.1.1 on 2022-09-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courts", "0002_alter_court_court_type_alter_court_sport_facility"),
    ]

    operations = [
        migrations.AddField(
            model_name="court",
            name="closing_hour",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="court",
            name="opening_hour",
            field=models.TimeField(blank=True, null=True),
        ),
    ]