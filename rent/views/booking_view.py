from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from rent.models import Booking
from rent.forms import BookingForm


class AddNewBookingView(SuccessMessageMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_message = 'The booking has been done'
    success_url = '/booking/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer = self.request.user
        return super(AddNewBookingView, self).form_valid(form)


class MyBookingHistory(ListView):
    model = Booking
    context_object_name = 'my_booking'
    template_name = 'booking/my_booking_history.html'

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)


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
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_message = 'The booking has been done'
    success_url = '/all-booking/'


class DeleteBookingView(SuccessMessageMixin, DeleteView):
    model = Booking
    success_message = 'The booking has been deleted'
    template_name = 'booking/delete_booking.html'
    success_url = '/all-booking/'