from .models import *
from rest_framework import serializers
class ZooSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zoo
        fields = ["name","location","price"]