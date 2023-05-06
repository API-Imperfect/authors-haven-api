from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(source="article.title", read_only=True)
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = Rating
        fields = ["id", "article_title", "user_first_name", "rating", "review"]
