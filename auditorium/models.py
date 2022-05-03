from datetime import datetime, timedelta

from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save

from movie.models import Movie
from auditorium.utils import schedule_task_to_update_reservations


class Auditorium(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    seats_no = models.PositiveIntegerField(default=112)

    def __str__(self):
        return self.name


class Seat(models.Model):
    ROW_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H')
    ]

    row = models.CharField(choices=ROW_CHOICES, max_length=1)
    number = models.PositiveIntegerField(validators=
                                        [MinValueValidator(1),
                                        MaxValueValidator(14)]
                                        )

    def __str__(self):
        return f'{self.row}{self.number}'


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.DO_NOTHING)
    screening_start_at = models.DateTimeField()


    def get_is_valid(self) -> bool:
        """
        We consider the instance "valid" if the current date and
        time haven't reached the value in "screening start".
        """
        return bool(self.screening_start_at > timezone.now())

    def get_estimated_finish(self):
        return self.screening_start_at + timedelta(minutes = self.movie.duration_min)


post_save.connect(schedule_task_to_update_reservations, sender=Screening)