from rest_framework import serializers

from vote import models


class UserAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id",)
