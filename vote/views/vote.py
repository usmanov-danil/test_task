from datetime import datetime

import pytz
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from vote import models
from vote.serializers.vote import VoteSerializer

__all__ = ("VoteViewSet",)


class VoteViewSet(ReadOnlyModelViewSet):
    """Returns list of active votes"""
    serializer_class = VoteSerializer
    queryset = models.Vote.objects.filter(start_date__lte=datetime.now(tz=pytz.timezone("Europe/Moscow")),
                                          end_date__gte=datetime.now(tz=pytz.timezone("Europe/Moscow")))
