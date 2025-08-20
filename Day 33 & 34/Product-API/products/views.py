from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

# ✅ Pagination class (10 items per page)
class ProductPagination(PageNumberPagination):
    page_size = 10  # Show 10 products per page
    page_size_query_param = 'page_size'  # Optional override via query param

# ✅ API view with filters, ordering, and pagination
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    # Filter backends for filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering by category (exact match)
    filterset_fields = ['category']

    # Searching by name and category (partial match)
    search_fields = ['name', 'category']

    # Allow ordering by price or name (asc/desc using "-" prefix)
    ordering_fields = ['price', 'name']
