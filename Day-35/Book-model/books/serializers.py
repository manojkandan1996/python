# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_date", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
