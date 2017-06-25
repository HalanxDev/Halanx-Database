from rest_framework import serializers
from .models import Store
from Products.serializers import ProductSerializer


class StoreSerializer(serializers.ModelSerializer):

    ProductsAvailable = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = '__all__'



