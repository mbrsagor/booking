from django.urls import path
from rent.views import location_view, rent_view

urlpatterns = [
    # Location
    path('', location_view.Dashboard.as_view(), name='dashboard'),
    path('location/', location_view.LocationListView.as_view(), name='location_listview'),
    path('location-create/', location_view.LocationCreateView.as_view(), name='location_create'),
    path('location-update/<pk>/', location_view.LocationUpdateView.as_view(), name='location_update'),
    path('location-delete/<pk>/', location_view.LocationDeleteView.as_view(), name='location_delete'),
    # Rent
    path('rent/', rent_view.RentListView.as_view(), name='rent_listview'),
    path('create-rent/', rent_view.CreateRentView.as_view(), name='create_rent'),
    path('rent-update/<pk>/', rent_view.RentUpdateView.as_view(), name='rent_update'),
    path('rent-detail/<pk>/', rent_view.RentDetailsView.as_view(), name='rent_details'),
    path('rent-delete/<pk>/', rent_view.RentDeleteView.as_view(), name='rent_delete'),

]
