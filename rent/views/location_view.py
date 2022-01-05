from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.models import Location
from rent.form.rent_form import LocationForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationListView(ListView):
    model = Location
    template_name = 'location/location.html'
    context_object_name = 'location'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationCreateView(SuccessMessageMixin, CreateView):
    model = Location
    form_class = LocationForm
    success_message = 'Location created successful'
    template_name = 'location/location_create.html'
    success_url = '/location-create/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationUpdateView(SuccessMessageMixin, UpdateView):
    model = Location
    form_class = LocationForm
    success_message = 'Location updated successful'
    template_name = 'location/location_create.html'
    success_url = '/location/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationDeleteView(SuccessMessageMixin, DeleteView):
    model = Location
    success_message = 'The location has been deleted'
    template_name = 'location/location_delete.html'
    success_url = '/location/'
