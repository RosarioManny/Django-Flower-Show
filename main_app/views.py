# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Flowers, Watering
from .serializers import FlowersSerializer, WateringSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the Flower Show api home route!'}
    return Response(content)
  
class FlowerList(generics.ListCreateAPIView) :
  queryset = Flowers.objects.all()
  serializer_class = FlowersSerializer

class FlowerDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Flowers.objects.all()
  serializer_class = FlowersSerializer
  lookup_field = 'id'
  
class WaterListCreate(generics.ListCreateAPIView):
  serializer_class = WateringSerializer

  def get_queryset(self):
    flower_id = self.kwargs['flower_id']
    return Watering.objects.filter(flower_id=flower_id)
  
  def preform_create(self,serializer):

    flower_id = self.kwargs['flower_id']

    flower = Flowers.objects.get(id=flower_id)

    serializer.save(flower=flower)

class WateringDetails(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = WateringSerializer
  lookup_field = 'id'

  def get_queryset(self):
    flower_id = self.kwargs['flower_id']
    return Watering.objects.filter(flower_id=flower_id)