from unittest import TestCase
from unittest.mock import patch
import io

from game import boss_room_warning


class TestBossRoomWarning(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='q')
    def test_boss_room_warning_exit_choice(self, _, mock_output):
        with self.assertRaises(SystemExit):
            boss_room_warning()
        actual = mock_output.getvalue()
        expected = "calm coldness"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['123', '2'])
    def test_boss_room_invalid_input(self, _, mock_output):
        boss_room_warning()
        actual = mock_output.getvalue()
        expected = "input. Please enter 1"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['123', '2'])
    def test_boss_room_user_says_no(self, _, mock_output):
        boss_room_warning()
        actual = mock_output.getvalue()
        expected = "wise choice.."
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='1')
    def test_boss_room_user_check_return_on_yes(self, _):
        actual = boss_room_warning()
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_boss_room_user_check_return_on_no(self, _):
        actual = boss_room_warning()
        expected = False
        self.assertEqual(expected, actual)
