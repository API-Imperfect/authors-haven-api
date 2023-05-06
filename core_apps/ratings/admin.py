from django.contrib import admin

from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "article", "rating", "created_at", "updated_at"]


admin.site.register(Rating, RatingAdmin)
