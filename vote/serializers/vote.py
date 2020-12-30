from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from vote import models
from vote.serializers import question


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = "__all__"


class VoteUserSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = models.Vote
        fields = ("id", "description", "start_date", "end_date", "questions")

    @swagger_serializer_method(
        serializer_or_field=question.QuestionUserSerializer(many=True)
    )
    def get_questions(self, obj):
        objects = models.Question.objects.filter(id__in=obj.questions.all())
        return question.QuestionUserSerializer(
            objects, many=True, context=self.context
        ).data
