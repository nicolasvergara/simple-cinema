from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from auditorium.models import Screening, Seat
from reservation.services import reservation_create


class ReservationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    class ReservationSerializer(serializers.Serializer):
        screening = serializers.IntegerField()
        seat = serializers.IntegerField()

    def post(self, request):
        serializer = self.ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        screening_id = serializer.validated_data["screening"]
        seat_id = serializer.validated_data["seat"]

        reservation = reservation_create(request.user,
                                        screening_id,
                                        seat_id)
        return reservation