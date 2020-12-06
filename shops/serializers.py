#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers
from stations.serializers import StationSerializer

from .models import Shop


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # 外键字段 只读
    station = StationSerializer()
    class Meta:
        model = Shop
        fields = '__all__'
        depth = 2

