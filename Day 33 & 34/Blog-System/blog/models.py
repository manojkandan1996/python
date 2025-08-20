from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title
