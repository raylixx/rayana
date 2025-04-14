from django.contrib import admin

# Register your models here.

from apps.rent.models import *

# admin.site.register(Author)
admin.site.register(Apartment)

@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'album_count')
    list_display_links = ('name', 'album_count')
    list_filter = ('name', 'surname', 'album_count')
    search_fields = ('name', 'surname')
    ordering = ('id', 'name', 'surname')