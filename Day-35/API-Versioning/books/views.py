# books/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializerV1, BookSerializerV2
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        version = getattr(self.request, "version", "v1")
        # Normalize: sometimes version might be '1' or 'v1'
        v = str(version).lower()
        if v.startswith("v2") or v == "2":
            return BookSerializerV2
        return BookSerializerV1
