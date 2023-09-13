from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from magicaldayapi.models import MenuItem, Location

class MenuItemView(ViewSet):
    def list(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(
            menu_items, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        menu_item = MenuItem.objects.get(pk=pk)
        serialized = MenuItemSerializer(
            menu_item, many=False, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_menu_item = MenuItem()
        new_menu_item.name = request.data["name"]
        new_menu_item.description = request.data["description"]
        new_menu_item.price = request.data["price"]
        location = Location.objects.get(pk=request.data["location"])
        new_menu_item.location = location
        new_menu_item.image = request.data["image"]
        new_menu_item.save()
        return Response(MenuItemSerializer(new_menu_item).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        menu_item = MenuItem.objects.get(pk=pk)
        menu_item.name = request.data["name"]
        menu_item.description = request.data["description"]
        menu_item.price = request.data["price"]
        location = Location.objects.get(pk=request.data["location"])
        menu_item.location = location
        menu_item.image = request.data["image"]

        menu_item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        menu_item = MenuItem.objects.get(pk=pk)
        menu_item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'price', 'location', 'image')
        depth = 1