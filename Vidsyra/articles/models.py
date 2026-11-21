from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
    )
    source_video = models.ForeignKey(
        "videos.Video",
        on_delete=models.PROTECT,
        related_name="articles",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)
    introduction = models.TextField(blank=True)
    key_takeaways = models.JSONField(default=list, blank=True)
    sections = models.JSONField(default=list, blank=True)
    tags = models.JSONField(default=list, blank=True)
    reading_time_minutes = models.PositiveSmallIntegerField(default=1)
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        indexes = [
            models.Index(fields=["status", "-published_at"], name="article_status_pub_idx"),
            models.Index(fields=["category", "status"], name="article_category_status_idx"),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:260] or "article"
            candidate = base_slug
            suffix = 2
            queryset = type(self).objects.all()
            while queryset.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base_slug[:250]}-{suffix}"
                suffix += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
