import logging

from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .filters import ArticleFilter
from .models import Article, ArticleView, Clap
from .pagination import ArticlePagination
from .permissions import IsOwnerOrReadOnly
from .renderers import ArticleJSONRenderer, ArticlesJSONRenderer
from .serializers import ArticleSerializer, ClapSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ArticlePagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ArticleFilter
    ordering_fields = [
        "created_at",
        "updated_at",
    ]
    renderer_classes = [ArticlesJSONRenderer]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        logger.info(
            f"article {serializer.data.get('title')} created by {self.request.user.first_name}"
        )


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "id"
    renderer_classes = [ArticleJSONRenderer]
    parser_classes = [MultiPartParser, FormParser]

    def perform_update(self, serializer):
        instance = serializer.save(author=self.request.user)
        if "banner_image" in self.request.FILES:
            if (
                instance.banner_image
                and instance.banner_image.name != "/profile_default.png"
            ):
                default_storage.delete(instance.banner_image.path)
            instance.banner_image = self.request.FILES["banner_image"]
            instance.save()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        viewer_ip = request.META.get("REMOTE_ADDR", None)
        ArticleView.record_view(
            article=instance, user=request.user, viewer_ip=viewer_ip
        )

        return Response(serializer.data)


class ClapArticleView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Clap.objects.all()
    serializer_class = ClapSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        article_id = kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)

        if Clap.objects.filter(user=user, article=article).exists():
            return Response(
                {"detail": "You have already clapped on this article."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        clap = Clap.objects.create(user=user, article=article)
        clap.save()
        return Response(
            {"detail": "Clap added to article"},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, *args, **kwargs):
        user = request.user
        article_id = kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)

        clap = get_object_or_404(Clap, user=user, article=article)
        clap.delete()
        return Response(
            {"detail": "Clap removed from article"},
            status=status.HTTP_204_NO_CONTENT,
        )
