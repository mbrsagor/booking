from django.db import models


class BookingCalculationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(city='kolkata')
