from xmlrpc.client import ServerProxy
from rest_framework import serializers

from .models import Schedule

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Schedule
        fields = ('date', 'agent_id', 'agent_name','country', 'type', 'client_name','client_phone', 'hour')