from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomePageView(TemplateView):
    template_name = 'homepage/homepage.html'


class DashboardView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    template_name = 'dashboard/dashboard.html'
