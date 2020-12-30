from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from vote import models
from vote.serializers import answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionUserSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = models.Question
        fields = ("id", "text", "type", "answers")

    @swagger_serializer_method(
        serializer_or_field=answer.AnswerUserSerializer(many=True)
    )
    def get_answers(self, obj):
        objects = models.Question.objects.filter(
            id__in=self.context["answers_user"].all()
        )
        return answer.AnswerUserSerializer(objects, many=True).data
