from django.urls import path
from api.location_view import LocationAPIListCreateView

urlpatterns = [
    path('location/', LocationAPIListCreateView.as_view(), name='location'),
]
