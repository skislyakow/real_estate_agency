from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = [
        'address', 'price', 'new_building', 'construction_year', 'town'
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    search_fields = ['user__username', 'flat__address', 'text']
    list_display = ['user', 'flat', 'text']


admin.site.register(Complaint, ComplaintAdmin)
