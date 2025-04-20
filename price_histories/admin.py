from django.contrib import admin
from .models import PriceHistory

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('listing', 'price', 'currency', 'created_at')
    search_fields = ('listing__title',)
    list_filter = ('currency', 'created_at')
    readonly_fields = ('created_at',)
