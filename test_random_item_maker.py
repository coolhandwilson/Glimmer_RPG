from unittest import TestCase
from unittest.mock import patch

from game import random_item_maker


class TestRandomItemMaker(TestCase):

    @patch('random.randint', return_value=0)
    @patch('random.choices', return_value=['Grundar Mold'])
    def test_random_item_maker_single_empty_room_with_new_item_lower_boundary(self, _, __):
        game_board = {(0, 0): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Grundar Mold']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', return_value=14)
    @patch('random.choices', return_value=['Grundar Mold'])
    def test_random_item_maker_single_empty_room_with_new_item_standard_use(self, _, __):
        game_board = {(0, 0): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Grundar Mold']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', return_value=30)
    @patch('random.choices', return_value=['Grundar Mold'])
    def test_random_item_maker_single_empty_room_with_new_item_upper_boundary(self, _, __):
        game_board = {(0, 0): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Grundar Mold']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', return_value=31)
    def test_random_item_maker_single_empty_room_no_new_item_lower_boundary(self, _):
        game_board = {(0, 0): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Nothing']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', return_value=65)
    def test_random_item_maker_single_empty_room_no_new_item_standard_use(self, _):
        game_board = {(0, 0): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Nothing']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', return_value=100)
    def test_random_item_maker_single_empty_room_no_new_item_upper_boundary(self, _):
        game_board = {(0, 0): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Nothing']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', side_effect=[14, 20, 10])
    @patch('random.choices', return_value=['Grundar Mold', 'Stale Bread', 'Water'])
    def test_random_item_maker_multiple_empty_room_with_new_items(self, _, __):
        game_board = {(0, 0): ['Living Room', 'Nothing'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Grundar Mold'],
                    (0, 1): ['Living Room', 'Stale Bread'],
                    (0, 2): ['Living Room', 'Water']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', side_effect=[76, 54, 45])
    def test_random_item_maker_multiple_empty_room_no_new_items(self, _):
        game_board = {(0, 0): ['Den', 'Nothing'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Den', 'Nothing'],
                    (0, 1): ['Living Room', 'Nothing'],
                    (0, 2): ['Living Room', 'Nothing']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', side_effect=[14, 45, 13])
    @patch('random.choices', return_value=['Grundar Mold', 'Stale Bread'])
    def test_random_item_maker_multiple_empty_room_with_some_new_items(self, _, __):
        game_board = {(0, 0): ['Living Room', 'Nothing'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Grundar Mold'],
                    (0, 1): ['Living Room', 'Nothing'],
                    (0, 2): ['Living Room', 'Stale Bread']}
        self.assertEqual(expected, game_board)

    @patch('random.randint', side_effect=[30, 54])
    @patch('random.choices', return_value=['Grundar Mold'])
    def test_random_item_maker_mixed_empty_and_full_room_with_new_items(self, _, __):
        game_board = {(0, 0): ['Living Room', 'Stale Bread'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Stale Bread']}
        random_item_maker(game_board)
        expected = {(0, 0): ['Living Room', 'Stale Bread'],
                    (0, 1): ['Living Room', 'Grundar Mold'],
                    (0, 2): ['Living Room', 'Stale Bread']}
        self.assertEqual(expected, game_board)
