from django.contrib import admin
from core.models import Car, CarComment

__all__ = ['CarAdmin']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_per_page = 50
    list_display_links = ['id', 'name']


@admin.register(CarComment)
class CarCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
    search_fields = ['name']
    list_per_page = 50
    list_display_links = ['id', 'name']
    readonly_fields = ['created_at']
