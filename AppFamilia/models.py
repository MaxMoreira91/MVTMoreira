from django.db import models
import datetime
# Create your models here.

class Familia(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()
    nacimiento=models.DateField()