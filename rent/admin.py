from django.contrib import admin
from .models import Location, Rent, Booking, User, Profile

admin.site.register(Location)
admin.site.register(Rent)
admin.site.register(Booking)
admin.site.register(User)
admin.site.register(Profile)
