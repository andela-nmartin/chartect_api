from charts.models.axis_data import Axis_Data
from django.shortcuts import get_object_or_404
from project_charts_api.api.serializers import axis_data
from rest_framework import generics
from rest_framework.response import Response

class AxisData(generics.ListCreateAPIView):
    """
    A simple View for listing or retrieving axis data.
    """
    def list(self, request):
        queryset = Axis_Data.objects.all()
        serializer = axis_data.Axis_Data_Serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Axis_Data.objects.all()
        all_data = get_object_or_404(queryset, pk=pk)
        serializer = axis_data.Axis_Data_Serializer(all_data)
        return Response(serializer.data)