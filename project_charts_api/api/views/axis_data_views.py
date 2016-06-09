from charts.models.axis_data import Axis_Data
from project_charts_api.api.serializers import axis_data
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AxisData(APIView):
    """
    A simple View for listing or retrieving axis data.
    """
    def get_object(self, pk):
        try:
            return Axis_Data.objects.get(pk=pk)
        except Axis_Data.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = axis_data.Axis_Data_Serializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = axis_data.Axis_Data_Serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)