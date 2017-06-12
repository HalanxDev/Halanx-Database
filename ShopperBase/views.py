

from .models import Shopper
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ShopperSerializer
from rest_framework.response import Response

# create method for displaying all timeslots of a particular date
# have to use regex in urls.py


@api_view(['GET', 'POST'])
def shopper_list(request):

    if request.method == 'GET':
        shoppers = Shopper.objects.all()
        serializer = ShopperSerializer(shoppers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShopperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])
def shopper_id(request, no):

    try:
        part = Shopper.objects.get(PhoneNo=no)
    except Shopper.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopperSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShopperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






