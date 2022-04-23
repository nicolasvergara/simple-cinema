from posixpath import basename
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from reservation import views


router = DefaultRouter()
router.register('reservation', views.ReservationView, basename='reservation')

urlpatterns = [
    path('', include(router.urls))
]