#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Station
from .permissions import IsOwnerOrReadOnly
from .serializers import StationSerializer
from shops.serializers import ShopSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["GET"])
@authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def station_shop_list(request, pk):
    """
    获取、更新、删除一个课程
    :param request:
    :param pk:
    :return:
    """
    try:
        station = Station.objects.get(pk=pk)
    except Station.DoesNotExist:
        return Response(data={"msg": "No such station"}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == "GET":
            s = ShopSerializer(instance=station.shop_set.all(), many=True)
            return Response(data=s.data, status=status.HTTP_200_OK)