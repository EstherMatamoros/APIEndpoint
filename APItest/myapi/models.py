from http import client
from django.db import models

# Create your models here.
class Schedule(models.Model):
        date = models.DateField(auto_now=False)
        agent_id = models.CharField(max_length=10)
        agent_name= models.TextField(max_length=50)
        country = models.CharField(max_length=20, default='Country')
        type = models.TextField(max_length=255)
        client_name = models.TextField(max_length=50)
        client_phone = models. CharField(max_length=15)
        hour = models.TimeField(auto_now=False)

        def __str__(self):
                return self.client_name