from django.urls import path

from .views import RatingCreateView

urlpatterns = [
    path(
        "rate_article/<uuid:article_id>/",
        RatingCreateView.as_view(),
        name="rating-create",
    )
]
