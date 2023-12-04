from django.test import TestCase
from my_game_ranks.models import Game

class GameModelTest(TestCase):

    @classmethod
    def create_game_test(cls):
        #set up object
        Game.objects.create(title=title,picture=picture,ranking=ranking)

    def test_create_game(self):
        game = Game.objects.get(id=1)
        field_label = game._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_length(self):
        game = Game.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_picture_length(self):
        game = Game.objects.get(id=1)
        max_length = author._meta.get_field('picture').max_length
        self.assertEqual(max_length, 1000)

    def test_ranking_length(self):
        game = Game.objects.get(id=1)
        max_length = author._meta.get_field('ranking').max_length
        self.assertEqual(max_length, 200)