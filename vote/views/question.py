from rest_framework.viewsets import ModelViewSet

from vote import models
from vote.serializers.question import QuestionSerializer

__all__ = ("QuestionViewSet",)


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = models.Question.objects.all()
