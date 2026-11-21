from django.contrib import admin

from .models import GenerationJob


@admin.register(GenerationJob)
class GenerationJobAdmin(admin.ModelAdmin):
    list_display = ("id", "job_type", "status", "requested_by", "source_video", "created_at")
    list_filter = ("job_type", "status", "provider")
    search_fields = ("input_url", "source_video__youtube_id", "source_video__title", "error_message")
    readonly_fields = ("created_at", "updated_at", "started_at", "completed_at")
