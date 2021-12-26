from django.contrib import admin
from .models import Location, Rent, Booking, User

admin.site.register(Location)
admin.site.register(Rent)
admin.site.register(Booking)
admin.site.register(User)
