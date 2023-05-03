from django.urls import path

from .views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="article-list-create"),
    path(
        "<uuid:id>/",
        ArticleRetrieveUpdateDestroyView.as_view(),
        name="article-retrieve-update-destroy",
    ),
]
