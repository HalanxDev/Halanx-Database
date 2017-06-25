from rest_framework import serializers
from .models import Cart, CartItem
from Products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    Item = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'



