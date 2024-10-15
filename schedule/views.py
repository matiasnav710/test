from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TimeSlot
from .serializers import TimeSlotSerializer

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticated]
