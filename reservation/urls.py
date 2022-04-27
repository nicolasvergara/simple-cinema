from django.urls import path, include

from reservation import views


urlpatterns = [
    path('reservation/', views.ReservationView.as_view(), name="reservation"),
]