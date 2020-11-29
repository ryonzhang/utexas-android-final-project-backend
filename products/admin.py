from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "introduction", "rating")
    search_fields = list_display
    list_filter = list_display