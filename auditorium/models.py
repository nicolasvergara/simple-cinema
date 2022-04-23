from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from movie.models import Movie


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
    screening_start = models.DateTimeField()