from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import  Hospital
from .serializers import *
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST'])
def hospitals(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
