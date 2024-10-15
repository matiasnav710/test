from rest_framework import serializers
from .models import TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'day_of_week', 'start_time', 'stop_time', 'ids']