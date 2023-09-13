from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import RideDetails, Location 

class RideDetailsView(ViewSet):
    def list(self, request):
        ride_details = RideDetails.objects.all()
        serializer = RideDetailsSerializer(
            ride_details, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        ride_details = RideDetails.objects.get(pk=pk)
        serialized = RideDetailsSerializer(
            ride_details, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_ride_details = RideDetails()
        new_ride_details.operating = request.data["operating"]
        new_ride_details.height_requirement = request.data["height_requirement"]
        new_ride_details.duration = request.data["duration"]
        new_ride_details.location = Location.objects.get(pk=request.data["location"])
        new_ride_details.expected_wait_time = request.data["expected_wait_time"]
        new_ride_details.save()
        return Response(RideDetailsSerializer(new_ride_details).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        ride_details = RideDetails.objects.get(pk=pk)
        ride_details.operating = request.data["operating"]
        ride_details.height_requirement = request.data["height_requirement"]
        ride_details.duration = request.data["duration"]
        ride_details.location = Location.objects.get(pk=request.data["location"])
        ride_details.expected_wait_time = request.data["expected_wait_time"]
        ride_details.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        ride_details = RideDetails.objects.get(pk=pk)
        ride_details.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RideDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideDetails
        fields = ('id', 'operating', 'height_requirement', 'duration', 'location', 'expected_wait_time')
        depth = 1