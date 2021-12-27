from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from rent.models import Booking


class NewBookingView(ListView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'booking/new_booking.html'

    def get_queryset(self):
        return Booking.objects.filter(status=0)


class AllBookingView(ListView):
    model = Booking
    context_object_name = 'all_booking'
    template_name = 'booking/all_booking.html'


class UpdateBookingView(SuccessMessageMixin, UpdateView):
    model = Booking


class DeleteBookingView(SuccessMessageMixin, DeleteView):
    model = Booking
    success_message = 'The booking has been deleted'
    template_name = 'booking/delete_booking.html'
    success_url = '/all-booking/'
