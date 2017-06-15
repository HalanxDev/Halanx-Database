from rest_framework import serializers
from .models import Shopper, Documents


class ShopperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shopper
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'
