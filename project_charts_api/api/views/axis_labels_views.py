from charts.models.axis_labels import Axis_Labels
from project_charts_api.api.serializers import axis_labels_serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AxisLabels(APIView):
    """
    A simple View for listing or retrieving axis labels.
    """
    def get_object(self, pk):
        try:
            return Axis_Labels.objects.get(pk=pk)
        except Axis_Labels.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = axis_labels_serializer.Axis_Labels_Serializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = axis_labels_serializer.Axis_Labels_Serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AllAxisLabels(APIView):
    """
    Getting all axis data
    """
    def get_object(self):
        try:
            return Axis_Labels.objects.all()
        except Axis_Labels.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        queryset = self.get_object()
        serializer = axis_labels_serializer.Axis_Labels_Serializer(queryset, many=True)
        return Response(serializer.data)