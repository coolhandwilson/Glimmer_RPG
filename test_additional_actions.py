from unittest import TestCase
from unittest.mock import patch
import io

from game import additional_actions


class TestAdditionalActions(TestCase):

    @patch('builtins.input', side_effect=['2', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_additional_actions_check_single_argument_predicate_call_print_out(self, mock_output, _):
        character = {"Name": "Rocky", "Level": 1, "HP": 110, 'Max HP': 120, 'XP': 0, 'Inventory': ["Helm of the Deep"]}
        game_board = {(0, 0): ['Living Room', 'Nothing'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        additional_actions(game_board, character)
        actual = mock_output.getvalue()
        expected = "satchel contains the following"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['6', '1'])
    def test_additional_actions_check_two_argument_predicate_call_print_out(self, _):
        character = {"Name": "Rocky", 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ["Helm of the Deep"]}
        game_board = {(0, 0): ['Living Room', 'Stale Bread'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        additional_actions(game_board, character)
        expected = {'Inventory': ["Helm of the Deep", "Stale Bread"]}
        self.assertEqual(expected["Inventory"], character["Inventory"])

    @patch('builtins.input', side_effect=['asdfas', '6', '1'])
    def test_additional_actions_error_and_correct_input(self, _):
        character = {"Name": "Blazer", 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ["Helm of the Deep"]}
        game_board = {(0, 0): ['Living Room', 'Water'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        additional_actions(game_board, character)
        expected = {'Inventory': ["Helm of the Deep", "Water"]}
        self.assertEqual(expected["Inventory"], character["Inventory"])
