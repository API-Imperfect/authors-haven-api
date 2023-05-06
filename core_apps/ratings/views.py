from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from core_apps.articles.models import Article
from core_apps.ratings.exceptions import YouhaveAlreadyRated

from .models import Rating
from .serializers import RatingSerializer


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs.get("article_id")
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid article_id provided")
        else:
            raise ValidationError("article_id is required")

        try:
            serializer.save(user=self.request.user, article=article)
        except IntegrityError:
            raise YouhaveAlreadyRated
