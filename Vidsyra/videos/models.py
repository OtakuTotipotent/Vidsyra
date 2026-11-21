from django.db import models


class Video(models.Model):
    """Canonical record for a YouTube video known to Vidsyra."""

    youtube_id = models.CharField(max_length=11, unique=True)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    channel_id = models.CharField(max_length=128, blank=True)
    channel_title = models.CharField(max_length=255, blank=True)
    thumbnail_url = models.URLField(max_length=500, blank=True)
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    view_count = models.PositiveBigIntegerField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    raw_metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title or self.youtube_id


class VideoTranscript(models.Model):
    """Transcript text for a video, stored separately by language."""

    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="transcripts")
    language_code = models.CharField(max_length=16, default="en")
    text = models.TextField()
    source = models.CharField(max_length=64, blank=True)
    retrieved_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["video", "language_code"],
                name="unique_video_transcript_language",
            )
        ]

    def __str__(self) -> str:
        return f"{self.video.youtube_id} ({self.language_code})"
