from django.db import models
from django.conf import settings

from auditorium.models import Screening, Seat


class Reservation(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    reserved = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=None)


    def __str__(self):
        return f'{self.screening} - {self.buyer.first_name} - {self.paid}'


class SeatReserved(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    screening = models.ForeignKey(Screening, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.seat} - {self.reservation.paid}'