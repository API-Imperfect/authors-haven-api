from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core_apps.users.views import CustomUserDetailsView

schema_view = get_schema_view(
    openapi.Info(
        title="Authors Haven API",
        default_version="v1",
        description="API endpoints for Authors Haven API Course",
        contact=openapi.Contact(email="api.imperfect@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    path("api/v1/bookmarks/", include("core_apps.bookmarks.urls")),
    path("api/v1/responses/", include("core_apps.responses.urls")),
    path("api/v1/elastic/", include("core_apps.search.urls")),
]

admin.site.site_header = "Authors Haven API Admin"

admin.site.site_title = "Authors Haven API Admin Portal"

admin.site.index_title = "Welcome to Authors Haven API Portal"
