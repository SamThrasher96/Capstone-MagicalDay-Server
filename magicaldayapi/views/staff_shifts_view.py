from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import StaffShift, Staff

class StaffShiftView(ViewSet):
    def list(self, request):
        staff_shifts = StaffShift.objects.all()
        serializer = StaffShiftSerializer(
            staff_shifts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        staff_shift = StaffShift.objects.get(pk=pk)
        serialized = StaffShiftSerializer(
            staff_shift, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_staff_shift = StaffShift()
        new_staff_shift.staff = Staff.objects.get(pk=request.data["staff"])
        new_staff_shift.date = request.data["date"]
        new_staff_shift.start_time = request.data["start_time"]
        new_staff_shift.end_time = request.data["end_time"]
        new_staff_shift.save()
        return Response(StaffShiftSerializer(new_staff_shift).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        staff_shift = StaffShift.objects.get(pk=pk)
        staff_shift.staff = Staff.objects.get(pk=request.data["staff"])
        staff_shift.date = request.data["date"]
        staff_shift.start_time = request.data["start_time"]
        staff_shift.end_time = request.data["end_time"]
        staff_shift.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        staff_shift = StaffShift.objects.get(pk=pk)
        staff_shift.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = ('id', 'staff', 'date', 'start_time', 'end_time')
        depth = 1