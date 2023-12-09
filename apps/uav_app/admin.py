from django.contrib import admin
from .models import UCAV, AircraftCategory, Brand, Rental


# UCAVAdmin

@admin.register(UCAV)
class UCAVAdmin(admin.ModelAdmin):
    autocomplete_fields = ('brand', 'aircraft_category')
    list_display = ('brand', 'model', 'max_speed_mach', 'max_altitude_feet')
    list_editable = ('max_speed_mach', 'max_altitude_feet')
    list_filter = ('brand', 'aircraft_category')
    search_fields = ('brand__name', 'model', 'aircraft_category__name')


# AircraftCategoryAdmin
@admin.register(AircraftCategory)
class AircraftCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# BrandAdmin
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    list_editable = ('country', 'founded_year')  # Örnek olarak country ve founded_year düzenlenebilir
    search_fields = ('name', 'country')

# RentalAdmin
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('ucav', 'user', 'start_date', 'end_date', 'status')
    list_editable = ('status',)  # Örnek olarak price ve status düzenlenebilir
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('ucav__model', 'user__username')

