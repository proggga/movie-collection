from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):

    name=models.CharField(max_length=120)

    namerus=models.CharField(max_length=120)

    time_in_minutes=models.IntegerField()

    imdb_stat=models.FloatField()

    kinopoisk=models.FloatField()

    watched=models.BooleanField(default=False)

    users = models.ManyToManyField(User, related_name='movies')

    def set_watched(self):
        if not self.watched:
            self.watched = True
