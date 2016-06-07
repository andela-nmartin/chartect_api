from __future__ import unicode_literals
from charts.models import axis_labels

from django.db import models

# Create your models here.
class Axis_Data(models.Model):
    data_set_code = models.ForeignKey(axis_labels.Axis_Labels, on_delete=models.CASCADE)
    x = models.CharField(max_length=200)
    y = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name