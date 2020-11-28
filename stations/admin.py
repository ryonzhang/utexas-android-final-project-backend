#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django.contrib import admin

from .models import Station


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "introduction", "owner", "rating",'location','longitude','latitude')
    search_fields = list_display
    list_filter = list_display
