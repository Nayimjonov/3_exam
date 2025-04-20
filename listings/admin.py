from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'currency', 'condition', 'is_active', 'is_featured')
    search_fields = ('title', 'seller__username', 'car__make__name', 'car__model__name')
    list_filter = ('condition', 'currency', 'is_active', 'is_featured')
    list_editable = ('is_active', 'is_featured')
    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ('car',)
