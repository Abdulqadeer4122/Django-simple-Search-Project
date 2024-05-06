from django.db import models
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.IntegerField()
    rating = models.FloatField()
    number_in_stock = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre_name')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
