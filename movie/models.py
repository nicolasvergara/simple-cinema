from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    director = models.CharField(max_length=256)
    cast = models.CharField(max_length=1024)
    description = models.TextField()
    duration_min = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-date_added',)