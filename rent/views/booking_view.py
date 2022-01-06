from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.models import Booking
from rent.forms.booking_form import BookingForm
from rent.filters.filter import BookingFilter


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddNewBookingView(SuccessMessageMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_message = 'Congratulations! Your booking has been done.'
    success_url = '/booking/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer = self.request.user
        return super(AddNewBookingView, self).form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyBookingHistory(ListView):
    model = Booking
    context_object_name = 'my_booking'
    template_name = 'booking/my_booking_history.html'

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NewBookingView(ListView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'booking/new_booking.html'

    def get_queryset(self):
        return Booking.objects.filter(status=0)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AllBookingView(ListView):
    model = Booking
    context_object_name = 'all_booking'
    template_name = 'booking/all_booking.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UpdateBookingView(SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_message = 'The booking has been done'
    success_url = '/all-booking/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeleteBookingView(SuccessMessageMixin, DeleteView):
    model = Booking
    success_message = 'The booking has been deleted'
    template_name = 'booking/delete_booking.html'
    success_url = '/all-booking/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BookingFilerListView(View):

    def get(self, request):
        booking_list = Booking.objects.all()
        booking_filer = BookingFilter(request.GET, queryset=booking_list)
        template = 'booking/booking_filter.html'
        ctx = {'result': booking_filer}
        return render(request, template, ctx)
