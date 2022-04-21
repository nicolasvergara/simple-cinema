from django.contrib import admin

from auditorium import models


admin.site.register(models.Auditorium)
admin.site.register(models.Seat)
admin.site.register(models.Screening)
