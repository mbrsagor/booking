from django.urls import path
from api.location_api import LocationAPIListCreateView
from api.rent_api import RentAPIListCreateView, RentUpdateDetailDeleteAPIView

urlpatterns = [
    path('location/', LocationAPIListCreateView.as_view()),
    path('rent/', RentAPIListCreateView.as_view()),
    path('rent/<pk>/', RentUpdateDetailDeleteAPIView.as_view()),
]
