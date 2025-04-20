from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'listing', 'is_read', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'listing__title', 'content')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)

    list_editable = ('is_read',)
