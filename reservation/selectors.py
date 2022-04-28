from django.db.models.query import QuerySet
from django.db.models import Q

from reservation.models import Reservation


def reservation_available(screening, seat) -> bool:
    query = Q(screening__id=screening, seat__id=seat)
    
    return Reservation.objects.filter(query).exists()