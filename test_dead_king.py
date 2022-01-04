from unittest import TestCase
from game import dead_king


class TestDeadKing(TestCase):
    def test_dead_king_lower_bound_alive(self):
        king = {'Name': "Afflicted King", 'Damage': [15, 30], 'HP': 1}
        actual = dead_king(king)
        expected = False
        self.assertEqual(expected, actual)

    def test_dead_king_upper_bound_alive(self):
        king = {'Name': "Afflicted King", 'Damage': [15, 30], 'HP': 225}
        actual = dead_king(king)
        expected = False
        self.assertEqual(expected, actual)

    def test_dead_king_lower_bound_dead(self):
        king = {'Name': "Afflicted King", 'Damage': [15, 30], 'HP': -14}
        actual = dead_king(king)
        expected = True
        self.assertEqual(expected, actual)

    def test_dead_king_upper_bound_dead(self):
        king = {'Name': "Afflicted King", 'Damage': [15, 30], 'HP': 0}
        actual = dead_king(king)
        expected = True
        self.assertEqual(expected, actual)
