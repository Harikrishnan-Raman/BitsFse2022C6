from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import products
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
def prod_list(request):
    if request.method == 'GET':
        data = products.objects.all()

        serializer = productSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = productSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'GET'])
def prod_detail(request, pk):
    try:
        prod = products.objects.get(pk=pk)
    except products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = prod

        serializer = productSerializer(data, context={'request': request}, many=False)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = productSerializer(prod, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prod.delete()
        return Response(status=status.HTTP_200_OK)


