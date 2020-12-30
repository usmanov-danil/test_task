from rest_framework.viewsets import GenericViewSet, mixins

from vote import models
from vote.serializers import user

__all__ = ("UserAuthorizationViewSet", "UserSubmissionViewSet", "UserVotesViewSet")


class UserAuthorizationViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin
):
    """Returns id of created user"""

    serializer_class = user.UserAuthorizationSerializer
    queryset = models.CustomUser.objects.all()


class UserSubmissionViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    """Submit by id user's vote and answers"""

    serializer_class = user.UserSubmissionSerializer
    queryset = models.CustomUser.objects.all()


class UserVotesViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    """Returns votes, questions and answer in which user participated"""

    serializer_class = user.UserVotesSerializer
    queryset = models.CustomUser.objects.all()
