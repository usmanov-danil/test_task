# Generated by Django 2.2.10 on 2020-12-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20201230_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(blank=True, related_name='vote_answers', to='vote.Answer', verbose_name='Ответы'),
        ),
    ]