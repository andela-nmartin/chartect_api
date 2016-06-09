from charts.models import axis_labels
from rest_framework import serializers
 
 
class Axis_Labels_Serializer(serializers.ModelSerializer):
    class Meta:
        model = axis_labels.Axis_Labels
        fields = ('data_set_code', 'x_units', 'y_units',)
        write_only_fields = ('x_units', 'y_units',)
        read_only_fields = ('data_set_code',)
 