#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops import views

router = DefaultRouter()
router.register(prefix="shops", viewset=views.ShopViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("shops/<int:pk>/products", views.shop_products_list, name="shop-products"),
]
