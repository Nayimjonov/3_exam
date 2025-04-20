from django.contrib import admin
from .models import Dealer

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'rating', 'is_verified', 'created_at')
    search_fields = ('user__username', 'company_name')
    list_filter = ('is_verified', 'rating')
    list_editable = ('is_verified', 'rating')
    readonly_fields = ('logo',)


    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="100" height="100"/>'
        return "No Logo"
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Logo Preview'
