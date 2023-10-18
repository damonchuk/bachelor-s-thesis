from django.contrib import admin
from core.models import RentIssue

__all__ = ['RentIssueAdmin']


@admin.register(RentIssue)
class RentIssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'car_smart']
    search_fields = ['name']
    list_per_page = 50
    list_display_links = ['id', 'car_smart']

    def car_smart(self, obj):
        return obj.car.name
    car_smart.admin_order_field = 'car'
    car_smart.short_description = 'Car'
