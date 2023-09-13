from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import Guest

class GuestView(ViewSet):
    def list(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(
            guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        guests = Guest.objects.get(pk=pk)
        serialized = GuestSerializer(guests, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        guests = Guest.objects.get(pk=pk)
        guests.label = request.data["label"]

        guests.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        guests = Guest.objects.get(pk=pk)
        guests.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'user', 'profile_picture', 'height')
        depth = 1