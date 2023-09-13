from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import Location

class LocationView(ViewSet):
    def list(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(
            locations, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        location = Location.objects.get(pk=pk)
        serialized = LocationSerializer(
            location, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        location = Location.objects.get(pk=pk)
        location.name = request.data["name"]
        location.image = request.data["image"]
        location.capacity = request.data["capacity"]
        location.opening_time = request.data["opening_time"]
        location.closing_time = request.data["closing_time"]
        location.description = request.data["description"]

        location.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        location = Location.objects.get(pk=pk)
        location.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'image', 'capacity', 'opening_time', 'closing_time', 'description')
        depth = 1