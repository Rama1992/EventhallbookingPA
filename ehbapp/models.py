from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Profile
from EventHallBookingProject import settings


# Create your models here.
class EventHall(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.TextField()
    description = models.TextField(default="this is a event hall")
    phone_number = models.CharField(max_length=10)
    #is_reserved = models.NullBooleanField()

    def __str__(self):
        return self.name


class Reservations(models.Model):
    booked_hall_name = models.ForeignKey(EventHall, on_delete=models.CASCADE)
    booked_on_date = models.DateField()
    booked_customer_Name = models.ForeignKey('accounts.customuser', to_field='id', on_delete=models.CASCADE)
