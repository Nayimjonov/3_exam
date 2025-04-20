from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'fuel_type', 'transmission', 'color', 'mileage', 'engine_size', 'power', 'drive_type', 'vin', 'created_at', 'updated_at')
    search_fields = ('make__name', 'model__name', 'vin')
    list_filter = ('fuel_type', 'transmission', 'drive_type', 'year')
    list_editable = ('fuel_type', 'transmission', 'drive_type')

    filter_horizontal = ('features',)

admin.site.register(Car, CarAdmin)
