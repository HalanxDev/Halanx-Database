
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        obj = Order.objects.create(**validated_data)
        obj.save()
        return obj.id



