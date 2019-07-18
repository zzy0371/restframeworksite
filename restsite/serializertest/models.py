from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SerializerModel(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=50)
    desc = models.CharField(max_length=500)
    born_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

