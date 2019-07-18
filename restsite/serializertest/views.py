from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class SerializerModelViewSet(viewsets.ModelViewSet):
    queryset = SerializerModel.objects.all().order_by("-name")
    serializer_class = SerializerModelSerializers
