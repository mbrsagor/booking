def validate_rent_service(attrs):
    if 'name' in attrs > 1:
        return "Name must be more than 1 charter"
    else:
        pass


def validate_booking_service(attrs):
    if 'booking_date' in attrs > 'checkout_date':
        return "Booking date and checkout date something went to wrong."
    else:
        pass
