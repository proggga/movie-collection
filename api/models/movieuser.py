from django.db import models
from django.contrib.auth.models import User
from api.models.movie import Movie


class MovieUser(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='movieuser')

    movies_want_set = models.ManyToManyField(Movie,
                                             related_name='users_want',
                                             blank=True)

    movies_watched_set = models.ManyToManyField(Movie,
                                                related_name='users_watched',
                                                blank=True)

    def check_movie_in_list(self, queryset, movie):
        """check movie in queryset (WHAT)"""
        try:
            queryset.get(id=movie.id)
            return True
        except Movie.DoesNotExist:
            return False

    def check_movie_in_want_list(self, movie):
        """Check in want list"""
        return self.check_movie_in_list(self.movies_want_set, movie)

    def check_movie_in_watched_list(self, movie):
        """Check in watched list"""
        return self.check_movie_in_list(self.movies_watched_set, movie)

    def set_watched(self, movie):
        """Set watched movie (move from want -> watched"""
        if not self.check_movie_in_watched_list(movie):
            self.movies_watched_set.add(movie)
        if self.check_movie_in_want_list(movie):
            self.movies_want_set.remove(movie)

    @staticmethod
    def create_user(*args, **kwargs):
        """Create django user and pass it to new user"""
        django_user = User(*args, **kwargs)
        django_user.save()
        new_user = MovieUser(user=django_user)
        new_user.save()
        return new_user
