import django_filters
from rent.models import Booking


class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = ['phone_number', 'transaction_id', 'booking_date', 'status']
