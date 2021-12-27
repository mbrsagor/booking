from django.urls import path
from .views import Dashboard, LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('location/', LocationListView.as_view(), name='location_listview'),
    path('location-create/', LocationCreateView.as_view(), name='location_create'),
    path('location-update/<pk>/', LocationUpdateView.as_view(), name='location_update'),
    path('location-delete/<pk>/', LocationDeleteView.as_view(), name='location_delete'),
]
