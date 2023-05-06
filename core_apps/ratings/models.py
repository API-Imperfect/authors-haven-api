from django.contrib.auth import get_user_model
from django.db import models

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Rating(TimeStampedModel):
    RATING_CHOICES = [
        (1, "Poor"),
        (2, "Fair"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent"),
    ]
    article = models.ForeignKey(
        Article, related_name="ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review = models.TextField(blank=True)

    class Meta:
        unique_together = ("article", "user")
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return f"{self.user.first_name} rated {self.article.title} as {self.get_rating_display()}"
