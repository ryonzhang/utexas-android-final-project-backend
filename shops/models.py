#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.conf import settings
from django.db import models
from stations.models import Station


class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Name", verbose_name="Name")
    introduction = models.TextField(help_text="Introduction", verbose_name="Introduction")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                help_text="Owner", verbose_name="Owner")
    rating = models.IntegerField(help_text="Rating", verbose_name="Rating")
    num_of_comments = models.IntegerField(help_text="Number of Comments", verbose_name="Number of Comments")
    station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                help_text="Station", verbose_name="Station")
    features = models.TextField(help_text="Features", verbose_name="Features")
    category = models.TextField(help_text="Category", verbose_name="Category")
    thumbnail_url = models.TextField(help_text="Thumbnail URL", verbose_name="Thumbnail URL")
    image_url = models.TextField(help_text="Image URL", verbose_name="Image URL")
    started_at = models.DateTimeField(help_text="Started At",  verbose_name="Started At")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Shops"
        verbose_name_plural = verbose_name
        ordering = ("rating",)

    def __str__(self):
        return self.name
