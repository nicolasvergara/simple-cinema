from django.db import models
from django.conf import settings

from auditorium.models import Screening, Seat


class Reservation(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    screening = models.ForeignKey(Screening, on_delete=models.DO_NOTHING)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False, null=True)
    active = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.screening.movie} {self.buyer.first_name} - {self.paid}'

    def update_paid_field(self, value):
        self.paid = value
        self.save(update_fields=['paid'])