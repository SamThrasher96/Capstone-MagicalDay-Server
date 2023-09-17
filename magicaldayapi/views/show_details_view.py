from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import ShowDetails, Location

class ShowDetailsView(ViewSet):
    def list(self, request):
        show_details = ShowDetails.objects.all()
        serializer = ShowDetailsSerializer(
            show_details, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        show_details = ShowDetails.objects.get(pk=pk)
        serialized = ShowDetailsSerializer(
            show_details, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_show_details = ShowDetails()
        new_show_details.location = Location.objects.get(pk=request.data["location"])
        new_show_details.duration = request.data["duration"]
        new_show_details.cast_size = request.data["cast_size"]
        new_show_details.running = request.data["running"]
        new_show_details.save()
        return Response(ShowDetailsSerializer(new_show_details).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        show_details = ShowDetails.objects.get(pk=pk)
        show_details.location = Location.objects.get(pk=request.data["location"])
        show_details.duration = request.data["duration"]
        show_details.cast_size = request.data["cast_size"]
        show_details.running = request.data["running"]
        show_details.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        show_details = ShowDetails.objects.get(pk=pk)
        show_details.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ShowDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowDetails
        fields = ('id', 'location', 'duration', 'cast_size', 'running', 'show_name', 'show_image', 'show_description', 'show_open', 'show_close')
        depth = 1