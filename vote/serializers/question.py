from rest_framework import serializers

from vote import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = (
            "__all__"
        )
