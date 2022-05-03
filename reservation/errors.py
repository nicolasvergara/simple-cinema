from rest_framework.exceptions import ValidationError


def trigger_seat_unavailable_detail():
    raise ValidationError (detail={"error": "The seat selected is unavailable"})

def trigger_screening_unavailable_detail():
    raise ValidationError (detail={"error": "The screening selected is unavailable"})