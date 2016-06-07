from charts.models import axis_labels
from django.shortcuts import get_object_or_404
from project_charts_api.api.serializers import axis_labels
from rest_framework import viewsets
from rest_framework.response import Response

class AxisLabelsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = axis_labels.Axis_Labels.objects.all()
        serializer = axis_labels.Axis_Labels_Serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = axis_labels.Axis_Labels.objects.all()
        all_labels = get_object_or_404(queryset, pk=pk)
        serializer = axis_labels.Axis_Labels_Serializer(all_labels)
        return Response(serializer.data)