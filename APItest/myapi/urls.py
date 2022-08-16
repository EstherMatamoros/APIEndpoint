from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Schedules', views.ScheduleViewSet)

#Wire up the API using aoutomatic URL routing. 
# Additionally, we include login URLS for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework'))
]