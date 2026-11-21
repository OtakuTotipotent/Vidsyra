from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "author", "is_featured", "published_at")
    list_filter = ("status", "category", "is_featured")
    search_fields = ("title", "summary", "tags")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
