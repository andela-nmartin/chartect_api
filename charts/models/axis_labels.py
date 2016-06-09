from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Axis_Labels(models.Model):
    data_set_code = models.IntegerField(default=0)
    x_units = models.CharField(max_length=200)
    y_units = models.CharField(max_length=200)
    def __unicode__(self):
        return self.x_units