from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Axis_Labels(models.Model):
    data_set_code = models.IntegerField(default=0)
    x_units = models.CharField(max_length=200)
    y_units = models.CharField(max_length=200)

class Axis_Data(models.Model):
    data_set_code = models.ForeignKey(Axis_Labels, on_delete=models.CASCADE)
    x = models.CharField(max_length=200)
    y = models.IntegerField(default=0)
    