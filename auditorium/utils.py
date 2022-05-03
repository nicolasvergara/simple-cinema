import json

from django_celery_beat.models import PeriodicTask, CrontabSchedule


def schedule_task_to_update_reservations(sender,
                                         instance,
                                         created,
                                         *args,
                                         **kwargs
                                         ):
    dt = instance.get_estimated_finish()

    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=dt.hour,
        minute=dt.minute,
        day_of_month=dt.day,
        month_of_year=dt.month,
        timezone='America/Santiago')

    PeriodicTask.objects.create(
        crontab=schedule,
        name=f'Put expired reservations as not active #{instance.id}',
        task='reservation.tasks.put_expired_reservations_as_not_active',
        kwargs=json.dumps({'id': instance.id}),
        one_off=True)
