from rest_framework import serializers
from .models import Flowers, Watering

class FlowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flowers
        fields = '__all__'

class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watering
        fields = '__all__'