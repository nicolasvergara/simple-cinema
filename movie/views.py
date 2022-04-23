from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework import filters

from movie import serializers
from movie import models


class PostPagination(PageNumberPagination):
    page_size = 9


class MovieViewSet(ListAPIView):
    queryset = models.Movie.objects.filter(
                            on_billboard=True
                            ).order_by('-date_added')
    serializer_class = serializers.MovieSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['title', 'director', 'cast', 'description',]
    ordering_fields = ['date_added',]