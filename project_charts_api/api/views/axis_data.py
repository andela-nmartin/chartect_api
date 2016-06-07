from charts.models import axis_data
from django.shortcuts import get_object_or_404
from project_charts_api.api.serializers import axis_data
from rest_framework import viewsets
from rest_framework.response import Response

class AxisLabelsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = axis_data.Axis_Data.objects.all()
        serializer = axis_data.Axis_Data_Serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = axis_data.Axis_Data.objects.all()
        all_data = get_object_or_404(queryset, pk=pk)
        serializer = axis_data.Axis_Data_Serializer(all_data)
        return Response(serializer.data)