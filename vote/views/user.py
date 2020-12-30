from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet, mixins

from vote import models
from vote.serializers.user import UserAuthorizationSerializer

__all__ = ("UserAuthorizationViewSet",)


class UserAuthorizationViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    """Returns id of created user"""

    serializer_class = UserAuthorizationSerializer
    queryset = models.CustomUser.objects.all()