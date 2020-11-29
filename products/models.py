#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.conf import settings
from django.db import models
from shops.models import Shop


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Name", verbose_name="Name")
    introduction = models.TextField(help_text="Introduction", verbose_name="Introduction")
    rating = models.IntegerField(help_text="Rating", verbose_name="Rating")
    num_of_comments = models.IntegerField(help_text="Number of Comments", verbose_name="Number of Comments")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                                help_text="Shop", verbose_name="Shop")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                help_text="Owner", verbose_name="Owner")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price", verbose_name="Price")
    amount_left = models.IntegerField(help_text="Amount Left", verbose_name="Amount Left")
    amount_sold = models.IntegerField(help_text="Amount Sold", verbose_name="Amount Sold")
    features = models.TextField(help_text="Features", verbose_name="Features")
    category = models.TextField(help_text="Category", verbose_name="Category")
    thumbnail_url = models.TextField(help_text="Thumbnail URL", verbose_name="Thumbnail URL")
    image_url = models.TextField(help_text="Image URL", verbose_name="Image URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = verbose_name
        ordering = ("rating",)

    def __str__(self):
        return self.name
