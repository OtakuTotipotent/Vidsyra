from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class VidsyraUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal information", {"fields": ("email",)}),
    )
