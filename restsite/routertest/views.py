from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

"""
使用视图
"""
class ZooListView(generics.ListCreateAPIView):
    queryset = Zoo.objects.all().order_by("-price")
    serializer_class = ZooSerializers
class ZooDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zoo.objects.all().order_by("-price")
    serializer_class = ZooSerializers

"""
使用视图集
"""
class ZooViewSet(viewsets.ModelViewSet):
    queryset = Zoo.objects.all().order_by("-price")
    serializer_class = ZooSerializers
