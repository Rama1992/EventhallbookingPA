from django.contrib import admin
from ehbapp.models import EventHall, Reservations


class EventHallAdmin(admin.ModelAdmin):
    pass


class ReservationsAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(EventHall, EventHallAdmin)
admin.site.register(Reservations, EventHallAdmin)
