from django.test import TestCase
from api.models.movieuser import MovieUser
from api.models.movie import Movie

class UserTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super(UserTestCase, self).__init__(*args, **kwargs)

    def setUp(self):
        self.John = MovieUser.objects.create_user('John Wick', 'johnwick@google.com', 'password1234')
        self.Nick = MovieUser.objects.create_user('Nick Madson', 'nickmadson@google.com', 'password4321')
        self.John.save()
        self.Nick.save()

        self.Iron = Movie.objects.create(
            name='Iron Man',
            namerus='Железный человек',
            time_in_minutes=127,
            imdb_stat=7.9,
            kinopoisk=7.894
        )
        self.Redemption = Movie.objects.create(
            name='The Shawshank Redemption',
            namerus='Побег из Шоушенка',
            time_in_minutes=142,
            imdb_stat=9.3,
            kinopoisk=9.115,
        )
        self.PulpFiction = Movie.objects.create(
            name='Pulp Fiction',
            namerus='Криминальное чтиво',
            time_in_minutes=154,
            imdb_stat=8.9,
            kinopoisk=8.624
        )
        self.John.movies.add(self.Iron)
        self.John.movies.add(self.Redemption)
        self.Nick.movies.add(self.Redemption)
        self.Nick.movies.add(self.PulpFiction)
        self.John.save()
        self.Nick.save()

    def test_user_can_set_watched(self):
        self.John.
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
