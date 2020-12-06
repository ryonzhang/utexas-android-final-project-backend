#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers
from shops.serializers import ShopSerializer

from .models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # 外键字段 只读
    shop = ShopSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        depth = 2

