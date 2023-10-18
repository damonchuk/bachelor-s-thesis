from django.contrib import admin
from core.models import UserMessage

__all__ = ['UserMessageAdmin']


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_per_page = 50
    list_display_links = ['id', 'name']
