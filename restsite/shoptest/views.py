from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializers

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
