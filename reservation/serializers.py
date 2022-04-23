from rest_framework import serializers

from reservation import models
from auditorium.serializers import ScreeningSerializer


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reservation
        fields = ('screening', 'seat',)