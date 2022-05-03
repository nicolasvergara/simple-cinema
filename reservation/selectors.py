from django.db.models.query import QuerySet
from django.db.models import Q

from reservation.models import Reservation


def reservation_already_reserved(
    screening: int,
    seat: int
) -> bool:
    query = Q(screening__id=screening, seat__id=seat)

    return Reservation.objects.filter(query).exists()


def active_reservations_by_screening(
    screening: int
) -> QuerySet[Reservation]:
    query = Q(screening__id=screening, status='ACTIVE')

    return Reservation.objects.filter(query)
