from django.contrib import admin
from .models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('destination', 'departure_date', 'return_date')
    list_filter = ('destination',)
    search_fields = ('destination',)


admin.site.register(Trip, TripAdmin)
