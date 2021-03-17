from django.db import models

# Create your models here.


class Processor(models.Model):
    name = models.CharField(max_length=50)
    socket = models.CharField(max_length=20)
    frequency = models.IntegerField()
