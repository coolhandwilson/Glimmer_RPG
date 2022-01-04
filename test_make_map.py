from unittest import TestCase
from game import make_map


class TestMakeMap(TestCase):

    def test_make_map_standard_map(self):
        board = {
                (0, 0): ['Dark Room', 'Nothing'],
                (0, 1): ['Crypt', 'Stale Bread'],
                (1, 0): ['Treasure Room', 'Water'],
                (1, 1): ['Workshop', 'Grundar Mold']
            }
        expected = [[' [δ]', ' [ ]'], [' [ ]', ' [Ω]']]
        actual = make_map(board)
        self.assertEqual(expected, actual)

    def test_make_map_standard_map_with_special_items(self):
        board = {
            (0, 0): ['Dark Room', 'Nothing'],
            (0, 1): ['Crypt', 'Stale Bread', 'special item'],
            (1, 0): ['Treasure Room', 'Water', 'special item'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        expected = [[' [δ]', ' [¿]'], [' [¿]', ' [Ω]']]
        actual = make_map(board)
        self.assertEqual(expected, actual)
