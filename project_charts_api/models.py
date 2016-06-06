from django.db import models


class Axis_Data(models.Model):
    x = models.CharField(max_length=200)
    y = models.IntegerField(default=0)
    data_set_code = models.IntegerField(default=0)


class Axis_Labels(models.Model):
    data_set_code = models.ForeignKey(Axis_Data, on_delete=models.CASCADE)
    x_units = models.CharField(max_length=200)
    y_units = models.CharField(max_length=200)