# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Flowers

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the Flower Show api home route!'}
    return Response(content)
  
class FlowerList(generics.ListCreateAPIView)
  def Flowers

class FlowerDetails(generics.RetrieveUpdateDestroyAPIView)
  
