#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()
router.register(prefix="product", viewset=views.ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
