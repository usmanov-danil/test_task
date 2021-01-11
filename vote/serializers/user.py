from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from vote import models
from vote.serializers import vote


class UserAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id",)


class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = "__all__"


class UserVotesSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    class Meta:
        model = models.CustomUser
        fields = (
            "id",
            "votes",
        )

    @swagger_serializer_method(serializer_or_field=vote.VoteUserSerializer(many=True))
    def get_votes(self, obj):
        objects = models.Vote.objects.filter(id__in=obj.votes.all())
        self.context["answers_user"] = obj.answers
        return vote.VoteUserSerializer(objects, many=True, context=self.context).data
