from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('listing', 'is_primary', 'order', 'created_at')
    search_fields = ('listing__title',)
    list_filter = ('is_primary',)
    list_editable = ('is_primary', 'order')
    readonly_fields = ('created_at',)
