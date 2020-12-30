from rest_framework import serializers

from vote import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = "__all__"


class AnswerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = "__all__"
