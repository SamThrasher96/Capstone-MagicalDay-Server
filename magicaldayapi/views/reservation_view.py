from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import Reservation, Guest, location_model

class ReservationView(ViewSet):
    def list(self, request):
        reservations = []
        reservations = Reservation.objects.all()
        if "user" in request.query_params:
            guest = Guest.objects.get(user=request.auth.user)
            reservations  = reservations.filter(guest=guest)
        serializer = ReservationSerializer(
            reservations, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        reservation = Reservation.objects.get(pk=pk)
        serialized = ReservationSerializer(
            reservation, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_reservation = Reservation()
        new_reservation.location = location_model.Location.objects.get(pk=request.data["location"])
        new_reservation.guest = Guest.objects.get(user=request.auth.user)
        new_reservation.date = request.data["date"]
        new_reservation.time = request.data["time"]
        new_reservation.save()
        return Response(ReservationSerializer(new_reservation).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        reservation = Reservation.objects.get(pk=pk)
        reservation.location = location_model.Location.objects.get(pk=request.data["location"])
        reservation.guest = Guest.objects.get(user=request.auth.user)
        reservation.date = request.data["date"]
        reservation.time = request.data["time"]
        reservation.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'location', 'guest', 'date', 'time', 'reservation_location_name', 'reservation_image')
        depth = 1