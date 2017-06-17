
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.response import Response
import json, base64


@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        # print "abc"
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])
def product_id(request, pk):

    try:
        part = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




