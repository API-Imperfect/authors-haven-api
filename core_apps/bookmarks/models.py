from django.contrib.auth import get_user_model
from django.db import models

from core_apps.articles.models import Article

User = get_user_model()


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="bookmarks"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "article"]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.first_name} bookmarked {self.article.title}"
