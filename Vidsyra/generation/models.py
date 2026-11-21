from django.conf import settings
from django.db import models


class GenerationJob(models.Model):
    class JobType(models.TextChoices):
        BLOG = "blog", "Blog generation"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        SUCCEEDED = "succeeded", "Succeeded"
        FAILED = "failed", "Failed"

    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generation_jobs",
    )
    source_video = models.ForeignKey(
        "videos.Video",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generation_jobs",
    )
    article = models.OneToOneField(
        "articles.Article",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generation_job",
    )
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.BLOG)
    input_url = models.URLField(max_length=500)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)
    provider = models.CharField(max_length=64, blank=True)
    model_name = models.CharField(max_length=128, blank=True)
    prompt_version = models.CharField(max_length=32, blank=True)
    error_message = models.TextField(blank=True)
    input_payload = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "created_at"], name="generation_status_created_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.get_job_type_display()} #{self.pk} ({self.status})"
