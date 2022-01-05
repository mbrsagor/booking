from django.forms import ModelForm, TextInput, Select, DateInput

from rent.models import Rent, Booking


class BookingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['rent_name'].queryset = Rent.objects.filter(is_available=True)

    class Meta:
        model = Booking
        exclude = ('customer', 'customer_id',)
        fields = (
            '__all__'
        )
        widgets = {
            'rent_name': Select(attrs={'class': 'form-control', 'id': 'rent_name'}),
            'status': Select(attrs={'class': 'form-control', 'id': 'status'}),
            'payment_type': Select(attrs={'class': 'form-control', 'id': 'payment_type'}),
            'address': TextInput(
                attrs={'class': 'form-control', 'id': 'address', 'placeholder': 'Enter your valid address'}),
            'booking_purpose': TextInput(attrs={'class': 'form-control', 'id': 'address',
                                                'placeholder': 'What purpose do you want to booking?'}),
            'transaction_id': TextInput(attrs={'class': 'form-control', 'id': 'transaction_id',
                                               'placeholder': '#38fzs37sf747'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number',
                                             'placeholder': 'Which phone number management will contact you'}),
            'booking_date': DateInput(attrs={'class': 'form-control', 'id': 'booking_date', 'type': 'date'}),
            'checkout_date': DateInput(attrs={'class': 'form-control', 'id': 'booking_date', 'type': 'date'}),
        }
