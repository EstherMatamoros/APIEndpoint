import sched
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ScheduleSerializer
from .models import Schedule
# Create your views here.

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('client_name')
    serializer_class = ScheduleSerializer
