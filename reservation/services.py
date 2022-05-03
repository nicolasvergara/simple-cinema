import stripe

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import transaction

from rest_framework.response import Response

from reservation.models import Reservation
from reservation.selectors import reservation_already_reserved
from reservation import errors
from account.models import UserAccount
from auditorium.models import Screening, Seat


@transaction.atomic
def reservation_create(
    buyer: UserAccount,
    screening_id: int,
    seat_id: int,
    is_paid: bool = True,
    status: bool = 'ACTIVE'
) -> Reservation:
    screening = get_object_or_404(Screening, id=screening_id)
    seat = get_object_or_404(Seat, id=seat_id)

    if not screening.get_is_valid():
        raise errors.trigger_screening_unavailable_detail()

    is_reserved = reservation_already_reserved(screening.id, seat.id)

    if not is_reserved:
        charge = create_charge()
        if charge.paid:
            reservation = Reservation(
                buyer=buyer,
                screening=screening,
                seat=seat,
                is_paid=is_paid,
                status=status
            )
            reservation.full_clean()
            reservation.save()

            return Response({"id": reservation.id,
                             "paid": reservation.is_paid
                             })
    raise errors.trigger_seat_unavailable_detail()


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
