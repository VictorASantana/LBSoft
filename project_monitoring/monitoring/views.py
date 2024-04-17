from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Chair
from .serializers import ChairSerializer

# Create your views here.
class ChairView(ModelViewSet): 
    def create(self, request):
        serializer = Chair(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Chair.objects.create(**serializer.validated_data)
        serializer = ChairSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
       
        chair = Chair.objects.filter(pk=pk).first()
        chair.is_occupied = True
        chair.save()
        response_serializer = ChairSerializer(chair)
        
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        queryset = Chair.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ChairSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_all(self, request): 
        chair_list = Chair.objects.all()

        if not chair_list: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ChairSerializer(chair_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)