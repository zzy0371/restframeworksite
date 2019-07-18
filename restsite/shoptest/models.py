from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Good(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField(default=50)
    desc = models.CharField(max_length=100,default="暂无介绍")
    born_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    good = models.OneToOneField(Good,on_delete=models.CASCADE,null=True,blank=True)
    num = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username+"_car"