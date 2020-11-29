from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "introduction", "owner", "rating")
    search_fields = list_display
    list_filter = list_display