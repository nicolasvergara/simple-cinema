from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.response import Response


def trigger_seat_unavailable_detail():
    raise ValidationError (detail={"error": "The seat selected is unavailable"})