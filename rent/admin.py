from django.contrib import admin
from .models import Location, Rent, Booking

admin.site.register(Location)
admin.site.register(Rent)
admin.site.register(Booking)
