from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.TripListView.as_view(), name='list_trip'),
    path('new/', views.TripCreateView.as_view(), name='create_trip'),
    path('<int:pk>/edit/', views.TripUpdateView.as_view(), name='update_trip'),
    path('<int:pk>/delete/', views.TripDeleteView.as_view(), name='delete_trip'),
]

