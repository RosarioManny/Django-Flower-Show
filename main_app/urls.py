from django.urls import path
from .views import Home, FlowerList, FlowerDetails

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('flowers/', FlowerList.as_view(), name='Flower-List'),
  path('flowers/<int:id>', FlowerDetails.as_view(), name='Flower-Details'),
]