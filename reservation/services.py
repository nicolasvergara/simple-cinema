import stripe

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import transaction

from rest_framework.response import Response
from rest_framework import status

from reservation.models import Reservation
from reservation.selectors import reservation_available
from account.models import UserAccount
from auditorium.models import Screening, Seat


@transaction.atomic
def reservation_create(
    buyer: UserAccount,
    screening_id: int,
    seat_id: int,
    paid: bool = True,
    active: bool = True
) -> Reservation:

    screening = get_object_or_404(Screening, id=screening_id)
    seat = get_object_or_404(Seat, id=seat_id)
    is_avatible = reservation_available(screening.id, seat.id)

    if is_avatible:
        charge = create_charge()
        if charge.paid:
            reservation = Reservation.objects.create(
                buyer=buyer,
                screening=screening,
                seat=seat,
                paid=paid,
                active=active
            )
            return Response ({"id": reservation.id}, status=status.HTTP_201_CREATED)
    return Response ({"message": "The seat selected is unavailable."},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE)

def create_charge():
    """ ***DUMMY CHARGE 🤷‍♂️*** """
    # (1) Creates card Token to sign the transaction -> https://stripe.com/docs/api/tokens/create_card
    # (2) Creates a charge -> https://stripe.com/docs/api/charges/create

    stripe.api_key = settings.STRIPE_SECRET_KEY
    amount = 15
    currency = "usd"
    token = stripe.Token.create(
             card={
                "number": "4242424242424242",
                "exp_month": 4,
                "exp_year": 2023,
                "cvc": "314",
             },
            )

    return stripe.Charge.create(
           amount=int(amount*100),
           currency=currency,
           description="simple-cinema 🚶‍♂️",
           source=token.id
           )