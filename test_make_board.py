from unittest import TestCase
from unittest.mock import patch

from game import make_board


class TestMakeBoard(TestCase):

    @patch('random.choice', side_effect=['Dark Room',
                                         'Nothing',
                                         'Crypt',
                                         'Stale Bread',
                                         'Treasure Room',
                                         'Water',
                                         'Workshop',
                                         'Grundar Mold'])
    def test_make_board_standard_board(self, _):
        row = 2
        column = 2
        expected = {
            (0, 0): ['Dark Room', 'Nothing'],
            (0, 1): ['Crypt', 'Stale Bread'],
            (1, 0): ['Treasure Room', 'Water'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        actual = make_board(row, column)
        self.assertEqual(expected, actual)
