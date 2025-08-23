from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.id")
    author_username = serializers.ReadOnlyField(source="author.username")
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "content",
            "author",
            "author_username",
            "comments_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("slug", "author", "author_username", "comments_count", "created_at", "updated_at")

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.id")
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "content",
            "author",
            "author_username",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("author", "author_username", "created_at", "updated_at")
