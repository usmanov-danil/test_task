# Generated by Django 2.2.10 on 2020-12-30 11:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='type',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='vote.Question', verbose_name='Вопросы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Колличество проголосовавших'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='questions',
            field=models.ManyToManyField(related_name='vote_questions', to='vote.Question', verbose_name='Вопросы'),
        ),
    ]