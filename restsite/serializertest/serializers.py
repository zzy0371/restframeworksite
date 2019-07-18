from .models import SerializerModel
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import date,timedelta

class SerializerModelSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    price = serializers.FloatField(default=50)
    desc = serializers.CharField(max_length=50)
    # 设定为只读 则不可编辑
    born_time = serializers.DateField(read_only=True)
    # PrimaryKeyRelatedField 中many为False则表示多对一  否则为多对多
    user = serializers.PrimaryKeyRelatedField(many=False,queryset=User.objects.all())
    # TODO  如果想要页面显示默认时间值应该怎么做     如果有关联对象怎么做    URL媒体链接怎么做




    def create(self, validated_data):
        return SerializerModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.born_time = validated_data.get("born_time", instance.born_time)
        instance.save()
        return instance
