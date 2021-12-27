from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from rent.models import Booking


class NewBookingView(ListView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'booking/new_booking.html'

    def get_queryset(self):
        return Booking.objects.filter(status=0)
