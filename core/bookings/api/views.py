from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from bookings.models import Trip
from .serializers import TripSerializer


class TripViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = TripSerializer

    def list(self, request):
        qs = Trip.objects.all()
        ser_data = self.serializer_class(instance=qs, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        trip = get_object_or_404(Trip, pk=pk)
        ser_data = self.serializer_class(instance=trip, data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        trip = get_object_or_404(Trip, pk=pk)
        ser_data = self.serializer_class(instance=trip, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        trip = get_object_or_404(Trip, pk=pk)
        trip.delete()
        return Response({'message': 'Trip deleted'}, status=status.HTTP_204_NO_CONTENT)
