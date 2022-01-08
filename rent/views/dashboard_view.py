from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.models import Booking, User, Location, Rent
from rent.utils.average_price import booking_average_price


class DashboardView(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        booking = Booking.objects.all().order_by('-id')
        cancel_booking = Booking.objects.filter(status=1)
        pending_booking = Booking.objects.filter(status=0)
        due_booking = Booking.objects.filter(payment_type=7).count(),
        users = User.objects.all()
        customer = User.objects.filter(role=0).count(),
        locations = Location.objects.all()
        rents = Rent.objects.all()
        booking_status = Booking.objects.filter(customer=self.request.user)
        total_income = sum(booking.values_list('rent_name__price', flat=True))
        average_income = booking_average_price(booking.values_list('rent_name__price', flat=True))

        context = {
            'booking': booking,
            'users': users,
            'customer': int(customer[0]),
            'locations': locations,
            'due_booking': int(due_booking[0]),
            'rents': rents,
            'cancel_booking': cancel_booking,
            'pending_booking': pending_booking,
            'booking_status': booking_status,
            'total_income': total_income,
            'average_income': average_income,
        }
        return self.render_to_response(context)
    template_name = 'dashboard/dashboard.html'
