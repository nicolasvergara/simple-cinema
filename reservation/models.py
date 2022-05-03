from django.db import models
from django.conf import settings

from auditorium.models import Screening, Seat


class Reservation(models.Model):

    STATUS_CHOICES = (
    ("ACTIVE", "Active"),
    ("USED", "Used"),
    ("EXPIRED", "Expired"),
    )

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    screening = models.ForeignKey(Screening, on_delete=models.DO_NOTHING)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    is_paid = models.BooleanField(default=False, null=True)
    status = models.CharField(max_length=128, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.screening.movie} - {self.status}"