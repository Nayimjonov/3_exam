from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'phone', 'location', 'rating', 'created_at')
    search_fields = ('user__username', 'phone', 'location')
    list_filter = ('user_type', 'created_at')
    readonly_fields = ('created_at',)

    list_editable = ('user_type', 'rating')
