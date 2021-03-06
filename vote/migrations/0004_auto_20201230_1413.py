# Generated by Django 2.2.10 on 2020-12-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vote", "0003_auto_20201230_1412"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="question",
        ),
        migrations.AddField(
            model_name="question",
            name="answers",
            field=models.ManyToManyField(
                related_name="vote_answers", to="vote.Answer", verbose_name="Ответы"
            ),
        ),
    ]
