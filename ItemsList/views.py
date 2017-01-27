

from .models import ItemList
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ItemListSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def itemslist_list(request):

    if request.method == 'GET':
        carts = ItemList.objects.all()
        serializer = ItemListSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])
def itemslist_id(request, pk):

    try:
        part = ItemList.objects.get(pk=pk)
    except ItemList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemListSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def itemslist_id(request, pk):

    try:
        part = ItemList.objects.get(pk=pk)
    except ItemList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemListSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






