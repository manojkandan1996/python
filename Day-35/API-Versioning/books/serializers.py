# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializerV1(serializers.ModelSerializer):
    version = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_date", "version"]

    def get_version(self, obj):
        req = self.context.get("request")
        return getattr(req, "version", "v1") if req is not None else "v1"

class BookSerializerV2(serializers.ModelSerializer):
    version = serializers.SerializerMethodField()
    extra_note = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_date", "version", "extra_note"]

    def get_version(self, obj):
        req = self.context.get("request")
        return getattr(req, "version", "v2") if req is not None else "v2"

    def get_extra_note(self, obj):
        return "returned-by-v2"
