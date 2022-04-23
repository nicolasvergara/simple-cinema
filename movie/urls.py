from django.urls import path

from movie import views


urlpatterns = [
    path('movie/', views.MovieViewSet.as_view()),
]