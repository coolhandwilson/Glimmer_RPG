from unittest import TestCase
from unittest.mock import patch
import io

from game import get_class_choice


class TestGetClassChoice(TestCase):

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_class_choice_output_for_valid_input(self, mock_output, _):
        user = "Bob"
        get_class_choice(user)
        actual = mock_output.getvalue()
        expected = "Bob the Scout."
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value="q")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_class_choice_output_for_quit_input(self, mock_output, _):
        user = "Bob"
        with self.assertRaises(SystemExit):
            get_class_choice(user)
        actual = mock_output.getvalue()
        expected = " calm coldness grip"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["H1", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_class_choice_output_for_help_input(self, mock_output, _):
        user = "Bob"
        get_class_choice(user)
        actual = mock_output.getvalue()
        expected = "scouts use their stealth"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["24t6erwqvbverw", '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_class_choice_output_for_invalid_input(self, mock_output, _):
        user = "Bob"
        get_class_choice(user)
        actual = mock_output.getvalue()
        expected = " enter a number between 1 "
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_get_class_choice_return_value_correct_input(self, _):
        user = "Bob"
        actual = get_class_choice(user)
        expected = "Berserker"
        self.assertEqual(expected, actual)
