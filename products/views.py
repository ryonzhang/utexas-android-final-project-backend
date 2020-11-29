#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
