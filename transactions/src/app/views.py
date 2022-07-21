from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import  Transaction
from .serializers import *
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST'])
def transactions(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
