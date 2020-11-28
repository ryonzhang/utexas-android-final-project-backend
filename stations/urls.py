#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stations import views

router = DefaultRouter()
router.register(prefix="stations", viewset=views.StationViewSet)

urlpatterns = [
    path("", include(router.urls))
]
