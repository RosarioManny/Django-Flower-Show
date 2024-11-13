from django.urls import path
from .views import Home, FlowerList

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('flowers/', FlowerList.as_view(), name='flowershow')
]