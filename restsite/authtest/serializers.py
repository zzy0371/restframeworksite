from rest_framework import serializers
from .models import *
class AuthModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthModel
        fields = ["title","user","url"]