from django.urls import include, path
from rest_framework.routers import DefaultRouter

from vote.swagger import schema_view
from vote.views import answer, question, user, vote

router = DefaultRouter()

router.register("get_active_votes", vote.VoteViewSet, basename="get_active_votes")
router.register("get_user_id", user.UserAuthorizationViewSet, basename="get_user_id")
router.register("send_answers", user.UserSubmissionViewSet, basename="send_answers")
router.register("get_user_votes", user.UserVotesViewSet, basename="get_user_votes")

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
