from rest_framework.viewsets import ModelViewSet
from vote import models
from vote.serializers.answer import AnswerSerializer

__all__ = ("AnswerViewSet",)


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = models.Answer.objects.all()
