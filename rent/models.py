from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import TYPES, ROLE


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser, BaseEntity):
    email = models.EmailField(blank=True, unique=False)
    phone_number = models.CharField(max_length=14, unique=True)
    role = models.IntegerField(choices=ROLE.select_role(), default=ROLE.CUSTOMER.value)

    def __str__(self):
        return self.username


class Location(BaseEntity):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='location', blank=True, null=True)
    image = models.ImageField(upload_to='location/%y/%m', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name[:30]

    def get_children(self):
        return Location.objects.filter(parent=self)

    def children_count(self):
        return Location.objects.filter(parent=self).count()


class Rent(BaseEntity):
    name = models.CharField(max_length=120)
    bed_room = models.IntegerField(default=1)
    bath_room = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=3)
    discount_price = models.DecimalField(default=0.00, max_digits=5, decimal_places=3)
    rent_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='RentLocation')
    types = models.IntegerField(choices=TYPES.select_types(), default=TYPES.ROOM.value)
    is_available = models.BooleanField(default=True)
    is_ac = models.BooleanField(default=False)
    is_wifi = models.BooleanField(default=False)
    is_tv = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    is_lunch = models.BooleanField(default=False)
    is_dinner = models.BooleanField(default=False)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='rent/%y/%m')
    gallery_image = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)
    gallery_image2 = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)
    gallery_image3 = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)
    gallery_image4 = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)
    gallery_image5 = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)

    def __str__(self):
        return self.name[:30]


class Booking(BaseEntity):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookingCustomer')
    rent_name = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name='orderRent')
    address = models.TextField()
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    booking_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self):
        return f"Customer: {self.customer.username} => Rent: {self.rent_name.name} => Booking Date: {self.booking_date}"

    @property
    def total_day(self):
        return self.booking_date - self.checkout_date


class CheckOut(Booking):
    pass
