from django.contrib import admin

from .models import Response


class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
        "article",
        "parent_response",
        "content",
        "created_at",
    ]

    list_display_links = ["pkid", "id", "user"]


admin.site.register(Response, ResponseAdmin)
