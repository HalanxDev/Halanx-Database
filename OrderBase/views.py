
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import OrderSerializer
from OrderBase.models import Order
from ItemsList.models import OrderItem
from Carts.models import Cart
from UserBase.models import User
from Products.models import Product
from ShopperBase.models import Shopper
from ItemsList.serializers import OrderItemSerializer
import requests

# create a view for displaying all orders of a particular batch


@api_view(['GET', 'POST'])
def order_list(request):

    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = request.data

        cartno = Cart.objects.get(UserPhone=data['CustomerPhoneNo'])
        allitems = cartno.carts.all()
        itemurl = "http://localhost:8000/itemslist/"
        # itemurl = "http://ec2-34-208-181-152.us-west-2.compute.amazonaws.com/itemslist/"

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            cid = serializer.save()

            curr = Order.objects.get(id=cid)
            curr.Total = cartno.Total
            curr.DeliveryCharges = cartno.DeliveryCharges

            curr.save()

            for obj in allitems:

                context = {
                    "OList": curr,
                    "Item": obj.ProId,
                    "Quantity": obj.Quantity,
                    "SubTotal": obj.SubTotal,
                    "Notes": obj.Notes
                }

                r = requests.post(itemurl, context)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_items(request, pk):

    try:
        part = Order.objects.get(id=pk)
        allitems = part.items.all()
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderItemSerializer(allitems, many=True)
        return Response(serializer.data)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])
def order_id(request, pk):

    try:
        part = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_orders(request, pk):

    if request.method == 'GET':

        g = Order.objects.filter(CustomerPhoneNo=pk)
        serializer = OrderSerializer(g, many=True)
        return Response(serializer.data)
























