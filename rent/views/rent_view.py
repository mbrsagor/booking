from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from rent.models import Rent
from rent.forms import RentForm


class RentListView(ListView):
    model = Rent
    template_name = 'rent/rent_list.html'
    context_object_name = 'rent'


class CreateRentView(SuccessMessageMixin, CreateView):
    model = Rent
    form_class = RentForm
    template_name = 'rent/create_rent.html'
    success_message = 'The rent has been created.'
    success_url = '/create-rent/'


class RentUpdateView(SuccessMessageMixin, UpdateView):
    model = Rent
    form_class = RentForm
    success_message = 'The rent has been updated successful'
    template_name = 'rent/create_rent.html'
    success_url = '/rent/'


class RentDetailsView(DetailView):
    model = Rent
    template_name = 'rent/rent_details.html'
    context_object_name = 'rent'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy("dashboard"))
        return super(RentDetailsView, self).dispatch(request, *args, **kwargs)


class RentDeleteView(SuccessMessageMixin, DeleteView):
    model = Rent
    success_message = 'The rent has been deleted'
    template_name = 'rent/rent_delete.html'
    success_url = '/rent/'
