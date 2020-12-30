from rest_framework import serializers

from vote import models


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = "__all__"
