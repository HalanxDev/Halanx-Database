from rest_framework import serializers
from .models import Shopper, Slot


class ShopperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shopper
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = '__all__'


