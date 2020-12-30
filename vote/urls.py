from django.urls import include, path
from rest_framework.routers import DefaultRouter
from vote.swagger import schema_view
from vote.views import answer, vote, question

router = DefaultRouter()
# router.register("vote", vote.VoteViewSet, basename="vote")
router.register("question", question.QuestionViewSet, basename="question")
router.register("answer", answer.AnswerViewSet, basename="answer")

router.register("get_active_votes", vote.VoteViewSet, basename="get_active_votes")


api_urls = [*router.urls]


urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", include(api_urls)),
]
