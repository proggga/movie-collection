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

class MovieTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super(MovieTestCase, self).__init__(*args, **kwargs)
        self.movie_collection = {}

    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'user@test.com', 'password')
        self.user.save()
        self.movie_collection['Iron'] = Movie.objects.create(
            name='Iron Man',
            namerus='Железный человек',
            time_in_minutes=127,
            imdb_stat=7.9,
            kinopoisk=7.894
        )
        self.movie_collection['Redemption'] = Movie.objects.create(
            name='The Shawshank Redemption',
            namerus='Побег из Шоушенка',
            time_in_minutes=142,
            imdb_stat=9.3,
            kinopoisk=9.115,
            watched=True
        )
        self.movie_collection['PulpF'] = Movie.objects.create(
            name='Pulp Fiction',
            namerus='Криминальное чтиво',
            time_in_minutes=154,
            imdb_stat=8.9,
            kinopoisk=8.624
        )
        for key, movie in self.movie_collection.items():
            movie.save()
            self.user.movies.add(movie)
        self.user.save()

    def test_movie_can_check_watched(self):
        iron = self.movie_collection['Iron']
        iron.set_watched()
        self.assertTrue(iron.watched)

    def test_movie_still_watched(self):
        redemption = self.movie_collection['Redemption']
        self.assertTrue(redemption.watched)
        redemption.set_watched()
        self.assertTrue(redemption.watched)

    def test_movies_has_right_user(self):
        for movie in self.movie_collection.values():
            self.assertTrue(self.user in movie.users.all())

    def test_user_has_right_movies(self):
        self.assertTrue(set(self.user.movies.all()) == set(self.movie_collection.values()))
