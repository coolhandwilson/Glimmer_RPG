from unittest import TestCase
from unittest.mock import patch
import io

from game import get_user_action


class TestGetUserAction(TestCase):

    @patch('builtins.input', return_value='q')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_action_output_with_quit_input(self, mock_output, _):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        with self.assertRaises(SystemExit):
            get_user_action(character, game_board)
        actual = mock_output.getvalue()
        expected = " feel a calm coldness grip your heart and the call"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['0', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_action_output_with_help_input(self, mock_output, _):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        get_user_action(character, game_board)
        actual = mock_output.getvalue()
        expected = "'2' for East, and so on. You may enter "
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['asehgewr242442', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_action_output_with_invalid_input(self, mock_output, _):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        get_user_action(character, game_board)
        actual = mock_output.getvalue()
        expected = "again, Dolly Parton! You may "
        self.assertIn(expected, actual)

    @patch('game.additional_actions', return_value=None)
    @patch('builtins.input', side_effect=['5', '1'])
    def test_get_user_action_return_value_with_additional_action_input(self, _, __):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        actual = get_user_action(character, game_board)
        expected = '1'
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_get_user_action_return_value_with_valid_direction_input(self, _):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        actual = get_user_action(character, game_board)
        expected = '2'
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['24t43-90', '3'])
    def test_get_user_action_return_value_for_invalid_and_valid_input(self, _):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        actual = get_user_action(character, game_board)
        expected = '3'
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['0', '4'])
    def test_get_user_action_return_value_for_help_and_valid_input(self, _):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"Name": "Dolly Parton"}
        actual = get_user_action(character, game_board)
        expected = '4'
        self.assertIn(expected, actual)
