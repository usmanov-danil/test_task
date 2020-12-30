from datetime import datetime

import pytz
from django.contrib.auth.models import User
from django.db import models


class Answer(models.Model):
    text = models.TextField("Текст ответа", blank=False, null=False)
    votes = models.IntegerField("Колличество проголосовавших", default=0)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        db_table = "answer"

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.TextField("Текст вопроса", blank=False, null=False)
    type_choices = [
        ("text", 'Ответ с текстом'),
        ("one_variant", 'Ответ с выбором одного варианта'),
        ("multiple_variants", 'Ответ с выбором несколких вариантов'),
    ]
    type = models.CharField("Тип вопроса", max_length=250, null=False, choices=type_choices)

    answers = models.ManyToManyField(
        Answer, related_name="vote_answers", verbose_name="Ответы", blank=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        db_table = "question"

    def __str__(self):
        return f"{self.text}, тип: {self.type}"


class Vote(models.Model):
    name = models.CharField("Название", max_length=128, blank=False, null=False)
    description = models.TextField("Описание", blank=False, null=False)
    start_date = models.DateTimeField("Начало опроса", default=datetime.now(tz=pytz.timezone("Europe/Moscow")))
    end_date = models.DateTimeField("Конец опроса", blank=False, null=False)

    questions = models.ManyToManyField(
        Question, related_name="vote_questions", verbose_name="Вопросы", blank=False)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"
        db_table = "vote"

    def __str__(self):
        return f"{self.name} - {self.start_date}"


class CustomUser(models.Model):
    id = models.IntegerField("id", primary_key=True)
    votes = models.ManyToManyField(
        Vote, related_name="user_votes", verbose_name="Опросы", blank=True)
    answers = models.ManyToManyField(
        Answer, related_name="vote_answer", verbose_name="Ответы", blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "custom_user"

    def __str__(self):
        return self.id
