from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    # file = models.FileField()
    
class car(models.Model):
    name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)
