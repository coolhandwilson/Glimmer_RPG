from unittest import TestCase
from unittest.mock import patch

from game import validate_move


class TestValidateMove(TestCase):

    def test_validate_move_return_value_for_valid_move_not_boss_room(self):
        game_board = {(0, 0): ['Living Room', 'Nothing'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        direction = '3'
        actual = validate_move(game_board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_return_value_for_invalid_move_not_boss_room(self):
        game_board = {(0, 0): ['Living Room', 'Soup'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        direction = '1'
        actual = validate_move(game_board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('game.boss_room_warning', return_value=True)
    def test_validate_move_return_value_for_valid_move_at_boss_room_fight_boss(self, _):
        game_board = {(0, 0): ['Living Room', 'Stale Bread'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {"X-Coordinate": 0, "Y-Coordinate": 1}
        direction = '3'
        actual = validate_move(game_board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    @patch('game.boss_room_warning', return_value=False)
    def test_validate_move_return_value_for_valid_move_at_boss_avoid_fight_boss(self, _):
        game_board = {(0, 0): ['Living Room', 'Water'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {"X-Coordinate": 0, "Y-Coordinate": 1}
        direction = '3'
        actual = validate_move(game_board, character, direction)
        expected = False
        self.assertEqual(expected, actual)
