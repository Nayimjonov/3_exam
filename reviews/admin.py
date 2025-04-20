from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'reviewed_user', 'listing', 'rating', 'created_at')
    search_fields = ('reviewer__username', 'reviewed_user__username', 'listing__title', 'comment')
    list_filter = ('rating', 'created_at')
    readonly_fields = ('created_at',)

    list_editable = ('rating',)
