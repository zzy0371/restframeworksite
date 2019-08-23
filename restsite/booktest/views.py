from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializes import BookSerializers,HeroSerializers
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-pub_time")
    serializer_class = BookSerializers

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers