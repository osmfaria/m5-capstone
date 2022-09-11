# Generated by Django 4.1.1 on 2022-09-09 00:37

import creditcards.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment_information",
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
                    "number",
                    django_cryptography.fields.encrypt(
                        creditcards.models.CardNumberField(
                            max_length=25, verbose_name="card number"
                        )
                    ),
                ),
                (
                    "code",
                    django_cryptography.fields.encrypt(
                        creditcards.models.SecurityCodeField(
                            max_length=4, verbose_name="security code"
                        )
                    ),
                ),
                (
                    "expiration_date",
                    django_cryptography.fields.encrypt(
                        models.CharField(max_length=250)
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_informations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
