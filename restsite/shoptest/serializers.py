from rest_framework import serializers
from .models import Good,Cart
class GoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ["title","price","desc","born_time","url"]

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["user","good","num","url"]