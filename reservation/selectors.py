from django.db.models.query import QuerySet
from django.db.models import Q

from reservation.models import Reservation


def reservation_available(screening, seat) -> bool:
    query = Q(screening__id=screening, seat__id=seat)
    qs = Reservation.objects.filter(query)
    if qs.count() >= 1:
        return False
    else:
        return True