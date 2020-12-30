from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Vote API",
        default_version="v0.0.1",
        description="API Vote app description",
        contact=openapi.Contact(email="usmanovdanilr@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
