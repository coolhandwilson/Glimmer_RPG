from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_with_move_on_y_axis(self):
        character = {"X-Coordinate": 0, "Y-Coordinate": 1}
        direction = '1'
        move_character(character, direction)
        expected = {"X-Coordinate": 0, "Y-Coordinate": 0}
        self.assertEqual(expected, character)

    def test_move_character_with_move_on_x_axis(self):
        character = {"X-Coordinate": 0, "Y-Coordinate": 1}
        direction = '2'
        move_character(character, direction)
        expected = {"X-Coordinate": 1, "Y-Coordinate": 1}
        self.assertEqual(expected, character)
