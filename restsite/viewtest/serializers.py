from rest_framework import serializers
from .models import *
class ViewModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViewModel
        fields = ["title","user"]