#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.conf import settings
from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Name", verbose_name="Name")
    introduction = models.TextField(help_text="Introduction", verbose_name="Introduction")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                help_text="Owner", verbose_name="Owner")
    rating = models.IntegerField(help_text="Rating", verbose_name="Rating")
    location = models.TextField(help_text="Location", verbose_name="Location")
    longitude = models.DecimalField(max_digits=6, decimal_places=2, help_text="Longitude", verbose_name="Longitude")
    latitude = models.DecimalField(max_digits=6, decimal_places=2, help_text="Latitude", verbose_name="Latitude")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "Stations"
        verbose_name_plural = verbose_name
        ordering = ("rating",)

    def __str__(self):
        return self.name
