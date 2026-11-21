from django.contrib import admin

from .models import Video, VideoTranscript


class VideoTranscriptInline(admin.StackedInline):
    model = VideoTranscript
    extra = 0


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("youtube_id", "title", "channel_title", "view_count", "created_at")
    search_fields = ("youtube_id", "title", "channel_title")
    readonly_fields = ("created_at", "updated_at")
    inlines = (VideoTranscriptInline,)


@admin.register(VideoTranscript)
class VideoTranscriptAdmin(admin.ModelAdmin):
    list_display = ("video", "language_code", "source", "retrieved_at")
    search_fields = ("video__youtube_id", "video__title", "text")
