from rest_framework import serializers
from .models import ItemList, Item


class ItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemList
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


