# Generated by Django 4.1.1 on 2022-09-21 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="timestamp",
            field=models.DateTimeField(
                blank=None,
                default=datetime.datetime(2022, 9, 21, 17, 4, 54, 906966),
                null=None,
            ),
        ),
    ]
