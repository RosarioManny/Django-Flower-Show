# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Flowers
from .serializers import FlowersSerializer

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
  lookup_field = id
  
  
