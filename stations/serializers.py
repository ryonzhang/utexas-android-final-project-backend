#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Station


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('name', 'introduction', 'owner', 'rating')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # 外键字段 只读

    class Meta:
        model = Station
        fields = '__all__'
        depth = 2

