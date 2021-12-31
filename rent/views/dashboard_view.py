from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.models import Booking, User, Location, Rent


class HomePageView(TemplateView):
    template_name = 'homepage/homepage.html'


class DashboardView(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        booking = Booking.objects.all().order_by('-id')
        cancel_booking = Booking.objects.filter(status=0)
        pending_booking = Booking.objects.filter(status=1)
        users = User.objects.all()
        locations = Location.objects.all()
        rents = Rent.objects.all()
        booking_status = Booking.objects.filter(customer=self.request.user)
        context = {
            'booking': booking,
            'users': users,
            'locations': locations,
            'rents': rents,
            'cancel_booking': cancel_booking,
            'pending_booking': pending_booking,
            'booking_status': booking_status,
        }
        return self.render_to_response(context)

    template_name = 'dashboard/dashboard.html'
