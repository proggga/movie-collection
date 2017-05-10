from django.test import TestCase
from api.models.movieuser import MovieUser
from api.models.movie import Movie

class UserTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super(UserTestCase, self).__init__(*args, **kwargs)

    def setUp(self):
        self.John = MovieUser.create_user(username='John Wick',
                                          email='johnwick@google.com',
                                          password='password1234')
        self.Nick = MovieUser.create_user(username='Nick Madson',
                                          email='nickmadson@google.com',
                                          password='password4321')
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
        self.John.movies_want_set.add(self.Iron)
        self.John.movies_want_set.add(self.Redemption)
        self.Nick.movies_want_set.add(self.Redemption)
        self.Nick.movies_want_set.add(self.PulpFiction)
        self.John.save()
        self.Nick.save()
