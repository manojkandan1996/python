from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from rest_framework.pagination import LimitOffsetPagination
from .models import Movie
from .serializers import MovieSerializer

# ✅ Custom Pagination
class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

# ✅ Inline FilterSet with 5 filters
class MovieFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact')  # exact match, case-insensitive
    release_date_after = django_filters.DateFilter(field_name='release_date', lookup_expr='gte')
    release_date_before = django_filters.DateFilter(field_name='release_date', lookup_expr='lte')
    rating_min = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_max = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['genre', 'release_date_after', 'release_date_before', 'rating_min', 'rating_max']

# ✅ ListAPIView with filters, pagination, and ordering
class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all().order_by('release_date', '-rating')  # default ordering
    serializer_class = MovieSerializer
    pagination_class = CustomPagination

    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filterset_class = MovieFilter
    ordering_fields = ['release_date', 'rating']  # enable sorting on these fields
