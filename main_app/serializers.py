from rest_framework import serializers
from .models import Flowers, Watering

class FlowersSerializer(serializers.ModelSerializer):
    watered_today = serializers.SerializerMethodField()

    class Meta:
        model = Flowers
        fields = '__all__'

    def get_watered_today(self, obj):
        return obj.watered_today()

class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watering
        fields = '__all__'
        read_only_fields = ('flowers',)