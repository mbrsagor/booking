import datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from rent.utils.enum import TYPES, ROLE, STATUS, PAYMENT, SEX, MARITAL


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser, BaseEntity):
    email = models.EmailField(blank=True, unique=False)
    phone_number = models.CharField(max_length=14, unique=True)
    role = models.IntegerField(choices=ROLE.select_role(), default=ROLE.CUSTOMER.value)

    def __str__(self):
        return self.username


class Profile(BaseEntity):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(blank=True, null=True)
    gender = models.IntegerField(choices=SEX.select_sex(), default=SEX.MALE.value)
    date_of_birth = models.DateField(blank=True, null=True, default=now)
    nid_number = models.IntegerField(default=123)
    marital_status = models.IntegerField(choices=MARITAL.select_status(), default=MARITAL.UNMARRIED.value)
    profile_picture = models.ImageField(upload_to='profile//%y/%m', blank=True, null=True)

    def __str__(self):
        return self.username.phone_number

    def calculate_age(self):
        age = datetime.date.today() - self.date_of_birth
        return int(age.days / 365.25)

    @property
    def make_full_name(self):
        return f"{self.username.first_name} {self.username.last_name}"

    @property
    def get_photo_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        else:
            return "/static/assets/images/faces/face8.jpg"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(username=instance)
        return profile


post_save.connect(create_user_profile, sender=User)


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
    price = models.IntegerField(default=0.00)
    discount_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=8)
    rent_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='RentLocation')
    types = models.IntegerField(choices=TYPES.select_types(), default=TYPES.ROOM.value)
    is_available = models.BooleanField(default=True)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='rent/%y/%m')
    gallery_image = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)
    gallery_image2 = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)
    gallery_image3 = models.ImageField(upload_to='rent/%y/%m', null=True, blank=True)

    def __str__(self):
        return self.name[:30]


class Booking(BaseEntity):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookingCustomer')
    rent_name = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name='orderRent')
    address = models.TextField()
    status = models.IntegerField(choices=STATUS.get_status(), default=STATUS.PENDING.value, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    booking_purpose = models.CharField(max_length=150, blank=True, null=True)
    payment_type = models.IntegerField(choices=PAYMENT.select_payment(), default=PAYMENT.DUE.value)
    booking_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self):
        return f"Customer: {self.customer.username} => Rent: {self.rent_name.name} => Booking Date: {self.booking_date}"

    @property
    def total_day(self):
        return int(self.checkout_date.strftime('%Y%m%d')) - int(self.booking_date.strftime('%Y%m%d'))

    @property
    def total_day_cost(self):
        return self.total_day * self.rent_name.price

    @property
    def total_calculation(self):
        return self.rent_name.price * Booking.objects.count()

    @property
    def average_calculation(self):
        return self.rent_name.price // Booking.objects.count()
