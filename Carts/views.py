

from .models import Cart
from .models import CartItem
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CartSerializer
from .serializers import CartItemSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def cart_list(request):

    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])
def cart_id(request, pk):

    try:
        part = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
@api_view(['GET'])
def cart_items(request, pk):

    try:

        # g = Cart.objects.get(pk=pk)
        # allitems = g.user_set.all()         error : 'Cart' object has no attribute 'user_set'
        # allitems = g.cartitem_set.all()     error : no attribute named 'Cart'
        # filter is used in case of many possible results

    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartItemSerializer(allitems)
        return Response(serializer.data)


"""

