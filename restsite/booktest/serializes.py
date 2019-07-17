from .models import *
from rest_framework import serializers
class BookSerializers(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = ["title","pub_time","url"]

class HeroSerializers(serializers.ModelSerializer):
    class Meta():
        model = Hero
        fields = ["name","skill","book","url"]