from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializes import BookSerializers,HeroSerializers
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-pub_time")
    serializer_class = BookSerializers

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers