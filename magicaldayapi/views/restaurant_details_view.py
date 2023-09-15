from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import RestaurantDetails, Location

class RestaurantDetailsView(ViewSet):
    def list(self, request):
        restaurant_details = RestaurantDetails.objects.all()
        serializer = RestaurantDetailsSerializer(
            restaurant_details, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        restaurant_details = RestaurantDetails.objects.get(pk=pk)
        serialized = RestaurantDetailsSerializer(
            restaurant_details, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_restaurant_details = RestaurantDetails()
        new_restaurant_details.location = Location.objects.get(pk=request.data["location"])
        new_restaurant_details.allergy_friendly = request.data["allergy_friendly"]
        new_restaurant_details.save()
        return Response(RestaurantDetailsSerializer(new_restaurant_details).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        restaurant_details = RestaurantDetails.objects.get(pk=pk)
        restaurant_details.location = Location.objects.get(pk=request.data["location"])
        restaurant_details.allergy_friendly = request.data["allergy_friendly"]
        restaurant_details.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        restaurant_details = RestaurantDetails.objects.get(pk=pk)
        restaurant_details.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RestaurantDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantDetails
        fields = ('id', 'location', 'allergy_friendly', 'restaurant_name', 'restaurant_image')
        depth = 1