from unittest import TestCase
from unittest.mock import patch
import io

from game import current_status


class TestCurrentStatus(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_current_status_with_character_and_no_foe(self, mock_output):
        snake = {"HP": 20, "Level": 1, "Max HP": 50, 'XP': 25}
        current_status(snake)
        actual = mock_output.getvalue()
        expected = "Max HP: 50"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_current_status_with_character_and_foe(self, mock_output):
        snake = {"HP": 20, "Level": 1, "Max HP": 50, 'XP': 25}
        enemy = {"HP": 20, "Name": 'Chuck'}
        current_status(snake, enemy)
        actual = mock_output.getvalue()
        expected = "Your HP: 20\t\t\t\tChuck"
        self.assertIn(expected, actual)
