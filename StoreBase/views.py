
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import StoreSerializer
from .models import Store
from Products.models import Product
from Products.serializers import ProductSerializer


# list of all stores
@api_view(['GET', 'POST'])
def store_list(request):

    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])    # localhost:8000/stores/pk
def store_id(request, pk):

    try:
        part = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StoreSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# to get products in a particular store
@api_view(['GET', 'PUT', 'DELETE'])     # localhost:8000/stores/pk/products
def store_products(request, pk):

    try:
        part = Product.objects.get(Store=pk)   # error
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(part, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # not needed put query
    '''
    elif request.method == 'PUT':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''













