from django.db import models

class Movie(models.Model):

    name=models.CharField(max_length=120)

    namerus=models.CharField(max_length=120)

    time_in_minutes=models.IntegerField()

    imdb_stat=models.FloatField()

    kinopoisk=models.FloatField()
