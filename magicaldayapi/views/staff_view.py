from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import Staff
from django.contrib.auth.models import User

class StaffView(ViewSet):
    def list(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(
            staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        staff = Staff.objects.get(pk=pk)
        serialized = StaffSerializer(staff, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        staff = Staff.objects.get(pk=pk)
        user = User.objects.get(pk=pk)
        staff.user = user
        staff.hired_on = request.data["hired_on"]
        staff.location = request.data["location"]
        staff.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'user', 'hired_on', 'location')
        depth = 1