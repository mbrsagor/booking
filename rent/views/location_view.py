from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from rent.models import Location
from rent.forms import LocationForm


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'


class LocationListView(ListView):
    model = Location
    template_name = 'location/location.html'
    context_object_name = 'location'


class LocationCreateView(SuccessMessageMixin, CreateView):
    model = Location
    form_class = LocationForm
    success_message = 'Location created successful'
    template_name = 'location/location_create.html'
    success_url = '/location-create/'


class LocationUpdateView(SuccessMessageMixin, UpdateView):
    model = Location
    form_class = LocationForm
    success_message = 'Location updated successful'
    template_name = 'location/location_create.html'
    success_url = '/location/'


class LocationDeleteView(SuccessMessageMixin, DeleteView):
    model = Location
    success_message = 'The location has been deleted'
    template_name = 'location/location_delete.html'
    success_url = '/location/'
