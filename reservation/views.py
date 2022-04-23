from locale import currency
import stripe

from django.conf import settings
from django.db import transaction

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from reservation import serializers
from reservation.models import Reservation


class ReservationView(viewsets.ModelViewSet):
    serializer_class = serializers.ReservationSerializer
    queryset = ''
    authentication_classes = (TokenAuthentication,)
    allowed_methods = ('post',)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                screening = serializer.validated_data.get('screening')
                seat = serializer.validated_data.get('seat')
                obj = Reservation.objects.filter(screening__id=screening.id,
                                                seat__id=seat.id
                                                )
                if obj:
                    return Response({'message': f'Seat {seat} is already reserved'},
                                    status=status.HTTP_400_BAD_REQUEST
                                    )
                payment_intent = create_charge()
                if payment_intent.paid:
                    serializer.save(buyer=request.user,
                                    paid=True)
                    return Response(serializer.data,
                                    status=status.HTTP_201_CREATED
                                    )
                return Response({'message': "Payment couldn't be accredited."},
                                status=status.HTTP_400_BAD_REQUEST
                                )
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                        )

def create_charge():
    # (1) Creates card Token to sign the transaction -> https://stripe.com/docs/api/tokens/create_card
    # (2) Creates a charge -> https://stripe.com/docs/api/charges/create

    stripe.api_key = settings.STRIPE_SECRET_KEY
    amount = 15
    currency = 'usd'
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
           description='simple-cinema 🚶‍♂️',
           source=token.id
           )