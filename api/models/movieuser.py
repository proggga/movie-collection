from django.db import models
from django.contrib.auth.models import User

from api.models.movie import Movie

class MovieUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='movieuser')

    movies_want_set = models.ManyToManyField(Movie, related_name='users_want', blank=True)

    movies_watched_set = models.ManyToManyField(Movie, related_name='users_watched', blank=True)

    def check_movie_in_list(self, queryset, movie):
        try:
            queryset.get(id=movie.id)
            return True
        except Movie.DoesNotExist:
            return False

    def check_movie_in_want_list(self, movie):
        return self.check_movie_in_list(self.movies_want_set, movie)

    def check_movie_in_watched_list(self, movie):
        return self.check_movie_in_list(self.movies_watched_set, movie)

    def set_watched(self, movie):
        if not self.check_movie_in_watched_list(movie):
            self.movies_watched_set.add(movie)
        if self.check_movie_in_want_list(movie):
            self.movies_want_set.remove(movie)
