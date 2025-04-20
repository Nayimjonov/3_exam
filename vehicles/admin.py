from django.contrib import admin
from .models import Make, Model, BodyType, Feature, Listing, SavedListing, ComparisonList

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'name')
    search_fields = ('make__name', 'name')
    list_filter = ('make',)

@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'make', 'model', 'price', 'created_at')
    search_fields = ('title', 'make__name', 'model__name', 'description')
    list_filter = ('make', 'model', 'created_at')

@admin.register(SavedListing)
class SavedListingAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing')
    search_fields = ('user__username', 'listing__title')

@admin.register(ComparisonList)
class ComparisonListAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
