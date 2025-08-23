from django.conf import settings
from django.db import models
from django.utils.text import slugify

def unique_slug(base: str, existing_slugs: set) -> str:
    base = slugify(base)[:50] or "post"
    if base not in existing_slugs:
        return base
    i = 2
    while True:
        candidate = f"{base}-{i}"
        if candidate not in existing_slugs:
            return candidate
        i += 1

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} (#{self.pk})"

    def save(self, *args, **kwargs):
        if not self.slug:
            existing = set(Post.objects.values_list("slug", flat=True))
            self.slug = unique_slug(self.title, existing)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"Comment #{self.pk} on {self.post_id} by {self.author_id}"
