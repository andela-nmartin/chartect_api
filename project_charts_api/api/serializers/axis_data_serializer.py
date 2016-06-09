from charts.models import axis_data
from rest_framework import serializers
 
 
class Axis_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = axis_data.Axis_Data
        fields = ('x', 'y', 'data_set_code',)
        write_only_fields = ('x', 'y',)
        read_only_fields = ('data_set_code',)
 