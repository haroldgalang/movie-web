from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.FloatField()
    poster = models.URLField(blank=True, default="https://via.placeholder.com/150")

    def __str__(self):
        return self.title
