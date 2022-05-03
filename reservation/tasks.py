from django.db import transaction

from celery import shared_task

from reservation import selectors


@shared_task()
@transaction.atomic
def put_expired_reservations_as_not_active(**kwargs):
    qs = selectors.active_reservations_by_screening(kwargs.get('id'))
    if qs:
        for obj in qs:
            obj.status = 'EXPIRED'
            obj.save(update_fields=['status'])