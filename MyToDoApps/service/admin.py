from django.contrib import admin
from service.models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'posted_date')  # Fields shown in the admin list view
    search_fields = ('title', 'property_type')  # Enables search functionality
    list_filter = ('property_type', 'furnishing')  # Adds filter options