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

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['booking'] = Booking.objects.all().order_by('-id')
        context['cancel_booking'] = Booking.objects.filter(status=0)
        context['pending_booking'] = Booking.objects.filter(status=1)
        context['users'] = User.objects.all()
        context['locations'] = Location.objects.all()
        context['rents'] = Rent.objects.all()
        return context

    template_name = 'dashboard/dashboard.html'
