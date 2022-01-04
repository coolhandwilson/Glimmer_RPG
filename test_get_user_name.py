import io
from unittest import TestCase
from unittest.mock import patch

from game import get_user_name


class TestGetUserName(TestCase):

    @patch('builtins.input', return_value="Bob")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_name_output_for_valid_input(self, mock_output, _):
        get_user_name()
        actual = mock_output.getvalue()
        expected = "A bump to the"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["12341234512", "Anne"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_name_output_for_invalid_input(self, mock_output, _):
        get_user_name()
        actual = mock_output.getvalue()
        expected = "memory? Please try"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='q')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_name_output_for_Quit_input(self, mock_output, _):
        with self.assertRaises(SystemExit):
            get_user_name()
        actual = mock_output.getvalue()
        expected = "calm coldness"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='Bob')
    def test_get_user_name_return_value_for_single_correct_input(self, _):
        expected = "Bob"
        actual = get_user_name()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['1313', 'Bob'])
    def test_get_user_name_return_value_for_invalid_and_valid_input(self, _):
        expected = "Bob"
        actual = get_user_name()
        self.assertIn(expected, actual)
