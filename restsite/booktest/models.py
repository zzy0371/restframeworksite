from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.CharField(max_length=20)
    skill = models.CharField(max_length=30)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

