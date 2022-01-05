from django.views.generic import TemplateView, DetailView

from rent.models import Location, Rent


class HomePageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['location'] = Location.objects.all()
        return context

    template_name = 'homepage/homepage.html'


class RentListPageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(RentListPageView, self).get_context_data(**kwargs)
        context['rent'] = Rent.objects.all()
        return context

    template_name = 'homepage/rent_list.html'


class RentDetailsView(DetailView):
    model = Rent
    context_object_name = 'rent'

    template_name = 'homepage/rent_details.html'
