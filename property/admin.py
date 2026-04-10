from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['complainant', 'flat']
    search_fields = ['complainant__username', 'flat__address', 'text']
    list_display = ['complainant', 'flat', 'text']


admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    search_fields = ['name', 'pure_phone', 'flats']
    list_display = ['name', 'owners_phonenumber', 'pure_phone']
    readonly_fields = ['pure_phone']


admin.site.register(Owner, OwnerAdmin)
