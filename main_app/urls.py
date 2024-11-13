from django.urls import path
from .views import Home, FlowerList, FlowerDetails, WaterListCreate, WateringDetails

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('flowers/', FlowerList.as_view(), name='Flower-List'),
  path('flowers/<int:id>', FlowerDetails.as_view(), name='Flower-Details'),
  path('flowers/<int:flower_id>/watering/', WaterListCreate.as_view(), name='watering-list-create'),
	path('flowers/<int:flower_id>/watering/<int:id>/', WateringDetails.as_view(), name='watering-details'),
]