import json

from celery import shared_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask


@shared_task()
def schedule_task_to_update_reservations(screening: int):
    from auditorium.models import Screening

    obj = Screening.objects.get(id=screening)
    execute_at = obj.estimated_finish()
    print("EXECUTED_ATTTTTTTTTTTTTTT")
    print(execute_at)
    """
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='30',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )
    
    PeriodicTask.objects.create(
    interval=schedule,                  
    name='Put expired reservations as not active',
    args=json.dumps([obj.id]),        
    task='reservation.tasks.put_expired_reservations_as_not_active',
    )
    """