import django_filters
from rent.models import Rent, Booking


class RentFilter(django_filters.FilterSet):
    class Meta:
        model = Rent
        fields = [
            'name', 'bed_room', 'bath_room', 'rent_location', 'types'
        ]


class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = ['phone_number', 'transaction_id', 'booking_date', 'status']
