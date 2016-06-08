from charts.models.axis_labels import Axis_Labels
from django.shortcuts import get_object_or_404
from project_charts_api.api.serializers import axis_labels
from rest_framework import generics
from rest_framework.response import Response

class AxisLabels(generics.ListCreateAPIView):
    """
    A simple View for listing or retrieving axis labels.
    """
    def list(self, request):
        queryset = Axis_Labels.objects.all()
        serializer = axis_labels.Axis_Labels_Serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Axis_Labels.objects.all()
        all_labels = get_object_or_404(queryset, pk=pk)
        serializer = axis_labels.Axis_Labels_Serializer(all_labels)
        return Response(serializer.data)