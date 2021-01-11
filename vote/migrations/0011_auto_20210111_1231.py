# Generated by Django 2.2.10 on 2021-01-11 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("vote", "0010_auto_20201230_1602"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="votes",
        ),
        migrations.AlterField(
            model_name="vote",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 1, 11, 9, 31, 10, 948249, tzinfo=utc),
                verbose_name="Начало опроса",
            ),
        ),
    ]
