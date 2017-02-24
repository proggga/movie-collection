from django.test import TestCase
from api.models.movie import Movie
from django.contrib.auth.models import User

class MovieTestCreationCase(TestCase):

    def test_movie_can_create(self):
        """Movie can be created"""
        iron_movie = Movie.objects.create(
            name='Iron Man',
            namerus='Железный человек',
            time_in_minutes=127,
            imdb_stat=7.9,
            kinopoisk=7.894
        )
        self.assertEqual(iron_movie.name, 'Iron Man')
