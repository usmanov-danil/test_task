# Generated by Django 2.2.10 on 2020-12-30 11:31

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("vote", "0006_auto_20201230_1426"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 12, 30, 11, 31, 31, 599130, tzinfo=utc),
                verbose_name="Начало опроса",
            ),
        ),
    ]
