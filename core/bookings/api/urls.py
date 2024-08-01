from django.urls import path
from . import views
from rest_framework import routers

app_name = 'bookings_api'
router = routers.SimpleRouter()
router.register('trips', views.TripViewSet)

urlpatterns = []

urlpatterns += router.urls
