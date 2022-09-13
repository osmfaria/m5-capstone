# Generated by Django 4.1.1 on 2022-09-13 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courts", "0009_alter_court_court_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="court",
            name="reference_number",
            field=models.IntegerField(
                default=1,
                unique=True,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
            preserve_default=False,
        ),
    ]
