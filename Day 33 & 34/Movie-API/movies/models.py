from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField()

    def __str__(self):
        return self.title
