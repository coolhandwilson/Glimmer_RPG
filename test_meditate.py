from unittest import TestCase
from unittest.mock import patch
import io

from game import meditate


class TestMeditate(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meditate_output_not_in_valid_room(self, mock_output):
        madonna = {"X-Coordinate": 0,
                   "Y-Coordinate": 1,
                   "Name": "Madonna",
                   "HP": 20,
                   "Level": 1,
                   "Max HP": 50,
                   "Prayer": 0}
        board = {(0, 0): ["Rest Area"], (0, 1): ["Living Room"]}
        meditate(board, madonna)
        actual = mock_output.getvalue()
        expected = "meditate, Madonna."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meditate_output_in_valid_room(self, mock_output):
        character = {"X-Coordinate": 0,
                     "Y-Coordinate": 0,
                     "Name": "Tina",
                     "HP": 20,
                     "Level": 1,
                     "Max HP": 50,
                     "Prayer": 0}
        board = {(0, 0): ["Rest Area"]}
        meditate(board, character)
        actual = mock_output.getvalue()
        expected = "calls to you, Tina"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meditate_output_prayer_setting_above_maximum(self, mock_output):
        character = {"X-Coordinate": 0,
                     "Y-Coordinate": 0,
                     "Name": "Cher",
                     "HP": 20,
                     "Level": 1,
                     "Max HP": 50,
                     "Prayer": 1}
        board = {(0, 0): ["Rest Area"]}
        meditate(board, character)
        actual = mock_output.getvalue()
        expected = "too long, Cher"
        self.assertIn(expected, actual)

    def test_meditate_change_to_character_not_in_valid_room(self):
        character = {"X-Coordinate": 0,
                     "Y-Coordinate": 1,
                     "Name": "Britney",
                     "HP": 20,
                     "Level": 1,
                     "Max HP": 50,
                     "Prayer": 0}
        board = {(0, 0): ["Rest Area"], (0, 1): ["Living Room"]}
        meditate(board, character)
        expected = {"X-Coordinate": 0,
                    "Y-Coordinate": 1,
                    "Name": "Britney",
                    "HP": 20,
                    "Level": 1,
                    "Max HP": 50,
                    "Prayer": 0}
        self.assertEqual(expected, character)

    def test_meditate_change_to_level_one_character_in_valid_room(self):
        character = {"X-Coordinate": 0,
                     "Y-Coordinate": 0,
                     "Name": "Madonna",
                     "HP": 20,
                     "Level": 1,
                     "Max HP": 50,
                     "Prayer": 0}
        board = {(0, 0): ["Rest Area"]}
        meditate(board, character)
        expected = {"X-Coordinate": 0,
                    "Y-Coordinate": 0,
                    "Name": "Madonna",
                    "HP": 30,
                    "Level": 1,
                    "Max HP": 50,
                    "Prayer": 1}
        self.assertEqual(expected, character)

    def test_meditate_change_to_level_three_character_in_valid_room(self):
        character = {"X-Coordinate": 0,
                     "Y-Coordinate": 0,
                     "Name": "Madonna",
                     "HP": 20,
                     "Level": 3,
                     "Max HP": 50,
                     "Prayer": 0}
        board = {(0, 0): ["Rest Area"]}
        meditate(board, character)
        expected = {"X-Coordinate": 0,
                    "Y-Coordinate": 0,
                    "Name": "Madonna",
                    "HP": 50,
                    "Level": 3,
                    "Max HP": 50,
                    "Prayer": 1}
        self.assertEqual(expected, character)

    def test_meditate_change_to_character_prayer_setting_above_maximum(self):
        character = {"X-Coordinate": 0,
                     "Y-Coordinate": 0,
                     "Name": "Madonna",
                     "HP": 20,
                     "Level": 1,
                     "Max HP": 50,
                     "Prayer": 1}
        board = {(0, 0): ["Rest Area"]}
        meditate(board, character)
        expected = {"X-Coordinate": 0,
                    "Y-Coordinate": 0,
                    "Name": "Madonna",
                    "HP": 20,
                    "Level": 1,
                    "Max HP": 50,
                    "Prayer": 1}
        self.assertEqual(expected, character)
